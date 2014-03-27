(function() {
    $.fn.calc = function() {
        return this.each(function() {
            var $this = $(this);

            function get_cookie(name) {
                var cookie_value = null;
                if (document.cookie && document.cookie != '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = $.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookie_value = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookie_value;
            }
            var csrftoken = get_cookie('csrftoken');

            function csrf_safe_method(method) {
                return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
            }

            function same_origin(url) {
                var host = document.location.host, // host + port
                    protocol = document.location.protocol,
                    sr_origin = '//' + host,
                    origin = protocol + sr_origin;
                // Allow absolute or scheme relative URLs to same origin
                return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
                    (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
                // or any other URL that isn't scheme relative or absolute i.e relative.
                !(/^(\/\/|http:|https:).*/.test(url));
            }

            function confirm_order(result) {
                $this.find('input#id').val(result.id);
                add_popup();
                $('.data_checking').load('/second/' + result.id + '/ .confirm');
            }

            if ($this.hasClass('calc')) {
                var hidden = $(this).find('input[type="hidden"]'),
                    select = $(this).find('select'),
                    select_without_lam = $(this).find('select[name="lamination"]');
                    checkbox = $(this).find('input[type="checkbox"]');
                hidden.not('.ratio').val(0);
                $this.find('input[name="count"]').val('');
                $this.find('input[name="count_hidden"]').val(0);
                select.each(function() {
                    var self = $(this),
                        self_name = $(this).attr('name'),
                        self_val = $(this).find('option:selected').data('price').replace(',', '.');
                    $this.find('input[name="' + self_name + '"]').val(self_val);
                    if(self_name == 'lamination') {
                        if($('option[value="1"]').prop('selected', true)){
                            checkbox.addClass('ronin').attr("disabled", true);
                        }
                    }
                });

                select.change(function() {
                    var self_name = $(this).attr('name'),
                        self_val = $(this).find('option:selected').data('price').replace(',', '.');
                    $this.find('input[name="' + self_name + '"]').val(parseFloat(self_val)).trigger('change');

                });
                if ($this.find('span.flag').length > 0) {
                    $('span.flag').click(function() {
                        var self = $(this),
                            self_id = $(this).attr('id');
                        self.toggleClass('active');
                        if (self.hasClass('active')) {
                            self.children('i').removeClass('fa-times').addClass('fa-check');
                            $this.find('input[name="' + self_id + '"]').val(parseFloat(self.data('price').replace(',', '.')));
                        } else {
                            if (self.children('i').hasClass('fa-check')) {
                                self.children('i').removeClass('fa-check').addClass('fa-times');
                            }
                            $this.find('input[name="' + self_id + '"]').val('0');
                        };
                        $this.find('input[name="' + self_id + '"]').trigger('change');
                    });
                    $this.find('small.question').click(function() {
                        $(this).toggleClass('active');
                    });
                } else {
                    checkbox.change(function() {
                        var self = $(this),
                            self_name = $(this).attr('name'),
                            self_val = $(this).data('price').replace(',', '.');
                        if (self.is(':checked')) {
                            $this.find('input[name="' + self_name + '"]').val(parseFloat(self_val));
                        } else {
                            $this.find('input[name="' + self_name + '"]').val(0);
                        }
                        $this.find('input[type="hidden"]').trigger('change');
                    });
                }
                $this.find('input[name="count"]').on("input", function() {
                    var self = $(this),
                        self_val = parseFloat($(this).val()) || 0;
                    if (self_val < 500) {
                        $this.find('input[name="count_hidden"]').val(0).trigger('change');
                    } else {
                        $this.find('input[name="count_hidden"]').val(parseFloat(self_val)).trigger('change');
                    };
                });
                if ($this.find('input[type="file"]').length > 0) {
                    $("#file_data").change(function() {
                        var options = {
                            url: '/uploadfile/',
                            replaceTarget: true,
                            target: $('#fd'),
                            success: function(data) {}
                        };
                        $this.ajaxSubmit(options);
                    });
                }
                hidden.change(function() {
                    var flag_val = 0,
                        count_val = parseFloat($this.find('input[name="count_hidden"]').val()),
                        color_val = parseFloat($this.find('input[name="colors"]').val()),
                        material_val = parseFloat($this.find('input[name="materials"]').val()),
                        lamination_val = parseFloat($this.find('input[name="lamination"]').val()),
                        face_color = parseFloat($this.find('input[name="color_front"]').val()),
                        back_color = parseFloat($this.find('input[name="color_back"]').val()),
                        total_colors = color_val + face_color + back_color;
                    $this.find('input.flag').each(function() {
                        flag_val += parseFloat($(this).val()) || 0;
                    });
                    var values = {},
                        range_array = [];
                    $this.find('input.ratio').each(function() {
                        var self_val = parseFloat($(this).val().replace(',', '.'));
                        self_name = parseFloat($(this).attr('name')),
                        q = count_val - self_name;
                        if (q > 0) {
                            values[self_val] = q;
                            range_array.push(q);
                        }
                    });
                    var min = Math.min.apply(null, range_array);
                    var z = 1;
                    $.each(values, function(key, value) {
                        if (value == min) {
                            z = parseFloat(key);
                        }
                    });
                    var sum = Math.ceil(parseFloat(z * count_val * (flag_val + total_colors + material_val + lamination_val)).toFixed(2));
                    $this.find('input[name="sum"]').val(sum);
                    $this.find('p.sum').html(sum + ' руб.');
                });
                $this.submit(function() {
                    $this.find('input[name="csrfmiddlewaretoken"]').val(csrftoken);
                    var action = $this.attr('action'),
                        selection = $this.find('input, select').not(' .ratio, input[name="colors"], input[name="materials"], input[name="count_hidden"], input[name="lamination"], input[name="color_front"], input[name="color_back"]').serialize();
                    if (valid == true) {
                        $.ajax({
                            url: action,
                            type: 'POST',
                            data: selection,
                            before_send: function(xhr, settings) {
                                if (!csrf_safe_method(settings.type) && same_origin(settings.url)) {
                                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                                }
                            },
                            success: function(result) {
                                if (valid == true) {
                                    confirm_order(result);
                                }
                            }
                        });
                    }
                    return false;
                });
            } else {
                $this.each(function() {
                    $(this).find('input[type="text"]').val('').on('input', function() {

                        var one_price = parseFloat($(this).siblings('span').children('small').html()),
                            count = parseFloat($(this).val()) || 0,
                            total = one_price * count,
                            total_fix = total.toFixed(2);
                        if (count <= 500) {
                            $(this).addClass('error').siblings('span').children('span').html('');
                        } else {
                            $(this).removeClass('error').siblings('span').children('span').html(total_fix + 'руб.');
                        }
                    });

                    $(this).submit(function() {
                        $(this).find('input[name="csrfmiddlewaretoken"]').val(csrftoken);
                        var self = $(this),
                            action = $(this).attr('action'),
                            self = $(this);
                        if (valid == true) {
                            $.ajax({
                                url: action,
                                type: 'POST',
                                data: self.serialize(),
                                before_send: function(xhr, settings) {
                                    if (!csrf_safe_method(settings.type) && same_origin(settings.url)) {
                                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                                    }
                                },
                                success: function(result) {
                                    if (valid == true) {
                                        confirm_order(result);
                                    }
                                }
                            });
                            return false;
                        } else {
                            return false;
                        }
                    });
                });

                function confirm_order(result) {
                    $(this).find('input#id').val(result.id);
                    add_popup();
                    $('.data_checking').load('/second/' + result.id + '/ .user_info',
                        function() {
                            valid = false;
                            $(this).find('form').valid();
                        }
                    );
                }
            }
        });
    }
}());