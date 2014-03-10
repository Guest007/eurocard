//Калькулятор
var valid = null;
(function() {
    $.fn.valid = function() {
        return this.each(function() {
            var $this = $(this);
            $this.find('input[type="submit"]').click(function() {
                var b = [];
                $this.find('input.for_valid').each(function() {
                    var self = $(this),
                        pattern,
                        error_text;
                    self_name = $(this).attr('name');
                    self_val = $(this).val();

                    function add_mes() {
                        b.push(0);
                        if (self.siblings('i').length == 0) {
                            self.parent().append('<i class="error show">' + error_text + '</i>');
                            self.siblings('i.error').css({
                                'left': self.parent().position().left,
                                'top': self.parent().position().top - 36
                            });
                        }
                    }
                    if (self_val == '') {
                        error_text = 'Поле не заполнено';
                        add_mes();
                    } else {
                        function check_function() {
                            if (self_val == '') {
                                add_mes();
                            } else if (self_val.match(pattern)) {
                                b.push(1);
                                self.siblings('i').remove();
                            } else {
                                error_text = 'Не верный формат данных';
                                add_mes();
                            }
                        }
                        if (self_name == 'count') {
                            pattern = /^\d+$/;
                            check_function();
                            if (self_val < 500) {
                                error_text = 'Минимальное значение - 500';
                                add_mes();
                            }
                        }
                        if (self_name == 'user') {
                            pattern = /^[a-zA-ZА-Яа-яЁё\s-]+$/;
                            check_function();
                        }
                        if (self_name == 'phone') {
                            pattern = /^\d+$/;
                            check_function();
                        }
                        if (self_name == 'email') {
                            pattern = /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,4}$/;
                            check_function();
                        }
                    }
                });
                if ($.inArray(0, b) > -1) {
                    valid = false;
                } else {
                    valid = true;
                }
            });
            $this.find('input.for_valid').on("input", function() {
                var self = $(this),
                    pattern,
                    error_text,
                    self_name = $(this).attr('name'),
                    self_val = $(this).val();

                function add_mes() {
                    if (self.siblings('i').length == 0) {
                        self.parent().append('<i class="error show">' + error_text + '</i>');
                        self.siblings('i.error').css({
                            'left': self.parent().position().left,
                            'top': self.parent().position().top - 36
                        });
                    }
                }
                self.siblings('i').remove();

                function check_function() {
                    if (self_val == '') {
                        error_text = 'Поле не заполнено';
                        add_mes();
                    } else if (self_val.match(pattern)) {
                        self.siblings('i').remove();
                    } else {
                        error_text = 'Не верный формат данных';
                        add_mes();
                    }
                }
                if (self_name == 'count') {
                    pattern = /^\d+$/;
                    check_function();
                    if (self_val < 500) {
                        error_text = 'Минимальное значение - 500';
                        add_mes();
                    }
                }
                if (self_name == 'user') {
                    pattern = /^[a-zA-ZА-Яа-яЁё\s-]+$/;
                    check_function();
                }
                if (self_name == 'phone') {
                    pattern = /^\d+$/;
                    check_function();
                }
                if (self_name == 'email') {
                    pattern = /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,4}$/;
                    check_function();
                }
            });
        });
    }
}());

(function() {
    $.fn.calc = function() {
        return this.each(function() {
            var $this = $(this);
            //valid = null;

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


            /*
            function validate() {
                $this.find('input[type="submit"]').click(function() {
                    var b = [];
                    $this.find('input.for_valid').each(function() {
                        var self = $(this),
                            pattern,
                            error_text;
                        self_name = $(this).attr('name');
                        self_val = $(this).val();

                        function add_mes() {
                            b.push(0);
                            if (self.siblings('i').length == 0) {
                                self.parent().append('<i class="error show">' + error_text + '</i>');
                                self.siblings('i.error').css({
                                    'left': self.parent().position().left,
                                    'top': self.parent().position().top - 36
                                });
                            }
                        }
                        if (self_val == '') {
                            error_text = 'Поле не заполнено';
                            add_mes();
                        } else {
                            function check_function() {
                                if (self_val == '') {
                                    add_mes();
                                } else if (self_val.match(pattern)) {
                                    b.push(1);
                                    self.siblings('i').remove();
                                } else {
                                    error_text = 'Не верный формат данных';
                                    add_mes();
                                }
                            }
                            if (self_name == 'count') {
                                pattern = /^\d+$/;
                                check_function();
                                if (self_val < 500) {
                                    error_text = 'Минимальное значение - 500';
                                    add_mes();
                                }
                            }
                            if (self_name == 'user') {
                                pattern = /^[a-zA-ZА-Яа-яЁё\s-]+$/;
                                check_function();
                            }
                            if (self_name == 'phone') {
                                pattern = /^\d+$/;
                                check_function();
                            }
                            if (self_name == 'email') {
                                pattern = /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,4}$/;
                                check_function();
                            }
                        }
                    });
                    if ($.inArray(0, b) > -1) {
                        valid = false;
                    } else {
                        valid = true;
                    }
                });
                $this.find('input.for_valid').on("input", function() {
                    var self = $(this),
                        pattern,
                        error_text,
                        self_name = $(this).attr('name'),
                        self_val = $(this).val();

                    function add_mes() {
                        if (self.siblings('i').length == 0) {
                            self.parent().append('<i class="error show">' + error_text + '</i>');
                            self.siblings('i.error').css({
                                'left': self.parent().position().left,
                                'top': self.parent().position().top - 36
                            });
                        }
                    }
                    self.siblings('i').remove();

                    function check_function() {
                        if (self_val == '') {
                            error_text = 'Поле не заполнено';
                            add_mes();
                        } else if (self_val.match(pattern)) {
                            self.siblings('i').remove();
                        } else {
                            error_text = 'Не верный формат данных';
                            add_mes();
                        }
                    }
                    if (self_name == 'count') {
                        pattern = /^\d+$/;
                        check_function();
                        if (self_val < 500) {
                            error_text = 'Минимальное значение - 500';
                            add_mes();
                        }
                    }
                    if (self_name == 'user') {
                        pattern = /^[a-zA-ZА-Яа-яЁё\s-]+$/;
                        check_function();
                    }
                    if (self_name == 'phone') {
                        pattern = /^\d+$/;
                        check_function();
                    }
                    if (self_name == 'email') {
                        pattern = /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,4}$/;
                        check_function();
                    }
                });
            }
*/
            if ($this.hasClass('calc')) {
                var hidden = $(this).find('input[type="hidden"]'),
                    select = $(this).find('select'),
                    checkbox = $(this).find('input[type="checkbox"]');
                //validate();
                hidden.not('.ratio').val(0);
                $this.find('input[name="count"]').val('');
                $this.find('input[name="count_hidden"]').val(0);
                select.each(function() {
                    var self = $(this),
                        self_name = $(this).attr('name'),
                        self_val = $(this).find('option:selected').data('price').replace(',', '.');
                    $this.find('input[name="' + self_name + '"]').val(self_val);
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
                    var sum = parseFloat(z * count_val * (flag_val + total_colors + material_val + lamination_val)).toFixed(2);
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
                    //validate();
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

                                //console.log(valid)
                                if (valid == true) {
                                    confirm_order(result);
                                }
                            }
                        });
                        return false;
                    });
                });

                function confirm_order(result) {
                    $(this).find('input#id').val(result.id);
                    add_popup();
                    $('.data_checking').load('/second/' + result.id + '/ .user_info',
                        function() {
                            valid = false;
                            //console.log(valid, 'ronin', $(this));
                            $(this).find('form').valid();
                        }
                    );
                }
            }
        });
    }
}());

function add_popup() {
    var s = 0,
        scrollDiv = document.createElement("div");
    scrollDiv.id = "mfp-sbm";
    scrollDiv.style.cssText = 'width: 99px; height: 99px; overflow: scroll; position: absolute; top: -9999px;';
    document.body.appendChild(scrollDiv);
    s = scrollDiv.offsetWidth - scrollDiv.clientWidth;
    document.body.removeChild(scrollDiv);

    $('html').addClass('hidden').css({
        'margin-right': s
    });
    //console.log(s);
    $('body').addClass('under_overlay')
        .append('<div class="overlay"></div><div class="data_wrap"><div><div class="data_container"><div class="data_checking"></div></div></div></div>');
}

//Формы
function form_style() {
    $('.jClever').jClever({
        selfClass: "alice",
        applyTo: {
            input: false,
            select: true,
            checkbox: true,
            radio: true,
            button: false,
            file: true,
            textarea: false
        },
    });
}

//Табы на главной, загрузка форм
function index_tabs() {
    var x = 0,
        y = 0;
    tabs_count = $('section.order > div > ul > li').length;
    $('section.order > div > ul > li').each(function() {
        x++;
        $(this).attr('id', x);
    });
    $('section.order > div > div').each(function() {
        y++;
        $(this).attr('rel', y);
        if ($(this).hasClass('current')) {
            $(this).load('/form_' + y + '/', function() {
                $(this).find('form').calc().valid();
            });
        }
    });
    $('section.order > div > ul > li').not('current').click(function() {
        var this_id = $(this).attr('id'),
            form_container = $('section.order > div > div[rel="' + this_id + '"]');
        $(this).addClass('current').siblings('li').removeClass('current');
        form_container.addClass('current').siblings('div').removeClass('current');
        if (form_container.children('form').length == 0) {
            form_container.load('/form_' + this_id + '/', function() {
                $(this).find('form').calc().valid();
                //$(this).find('ul').calc();
            });
        }
    });
}

//Выравнивание высоты заголовка новостей
function news_title_height() {
    var title_height = 0;
    $('section.news > ul > li > a').each(function() {
        var this_height = parseFloat($(this).height());
        if (this_height > title_height) {
            title_height = this_height;
        };
    });
    $('section.news > ul > li > a').height(title_height);
}

//Обратный звонок
function call_() {
    var $this = $('form.call'),
        valid;
    $('.location > div > a').click(function() {
        $this.removeClass('hide');
        return false;
    });
    $this.find('.close_form').click(function() {
        $this.addClass('hide').find('i').not('.fa').remove();
        $this.find('input[type="text"], textarea').val('');
    });
    $this.submit(function() {
        var action = $this.attr('action');
        $.ajax({
            url: action,
            type: 'POST',
            data: $this.serialize(),
            complete: function(result) {
                $this.addClass('hide');
                add_popup();
                $('.data_checking').addClass('thanks').html('<span>Ваша заявка принята.<small class="close_order"><i class="fa fa-times"></i></small></span><span>В ближайшее время наш сотрудник свяжется с вами по указанному в заявке номеру телефона.</span>');
            }
        });
        return false;
    });
}

//Смена адреса в раделе 'Контакты'
function change_adress() {
    var x = 0,
        y = 0,
        z = 0;
    $('div.contacts > div > span > a').each(function() {
        x++;
        $(this).attr('rel', x);
    });
    $('div.contacts > div > ul').each(function() {
        y++;
        $(this).attr('rel', y);
    });
    $('div.contacts > div > img').each(function() {
        z++;
        $(this).attr('rel', z);
    });
    $('div.contacts > div > span > a').not('current').click(function() {
        var this_rel = $(this).attr('rel');
        $(this).addClass('current').siblings().removeClass('current');
        $('div.contacts > div > ul[rel="' + this_rel + '"], div.contacts > div > img[rel="' + this_rel + '"]').addClass('current').siblings().removeClass('current');
        return false;
    });
}

$(document).ready(function() {

    index_tabs();

    news_title_height();

    call_();

    change_adress();

    //Тоглим таблиц с ценами в разделе 'Цены'
    $('a.show_price').click(function() {
        $(this).siblings('div.hide').slideToggle();
        return false;
    });

    //Заказ (закрываем модальное окно)
    $(document).on('click', '.close_order', function() {
        $('div.data_checking, div.overlay').remove();
        $('body, html').removeClass();
        $('html').css({
            'margin-right': 0
        });
    });
    $(document).on('click', '.close_order.reset', function() {
        document.location.href = "/";
    });

    //Подтверждение заказа.
    $(document).on('submit', '.last_step', function() {
        var action = $(this).attr('action'),
            self = $(this);
        if (valid == true) {
            $.ajax({
                url: action,
                type: 'POST',
                data: self.serialize(),
                complete: function(result) {
                    $('.data_checking').addClass('thanks').html('<span>Спасибо за ваш заказ.<small class="close_order reset"><i class="fa fa-times"></i></small></span><span>Письмо с информацией отправлено на указанный вами адрес электронной почты.</span><span>В ближайшее время наш сотрудник свяжется с вами для уточнения деталей.</span>');
                }
            });
            return false;
        } else {
            return false;
        };
    });

    //Убираем слэш
    $('div.ready > ul > li').each(function() {
        $(this).children().children('li').last().addClass('last');
    });

    //Клиенты(карусель)
    $('.carousel > div').carouFredSel({
        circular: false,
        infinite: false,
        auto: false,
        direction: 'left',
        align: 'left',
        prev: {
            button: '.clients > div > a.prev',
            key: 'left'
        },
        next: {
            button: '.clients > div > a.next',
            key: 'right'
        },
    });

});

//Глобальная загрузка Jclever для ajax контента
$(document).ajaxComplete(function(event, xhr, settings) {
    form_style();
});