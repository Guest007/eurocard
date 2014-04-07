(function() {
    $.fn.valid = function() {
        return this.each(function() {
            var $this = $(this),
                z = 0,
                x = 0;
            $this.find('input[type="submit"]').click(function() {
                var b = [];

                $this.find('input.for_valid').each(function() {
                    var self = $(this),
                        pattern,
                        error_text,
                        self_name = $(this).attr('name'),
                        self_val = $(this).val();

                    function add_mes() {
                        b.push(0);
                        if (self.siblings('i').length == 0) {
                            self.parent().append('<i class="error">' + error_text + '</i>');
                            self.siblings('i.error').css({
                                'left': self.parent().position().left
                            });
                            if (self.parents('#easy_form').length) {
                                self.siblings('i.error').css({
                                    'top': self.parent().position().top - 12
                                });
                            }
                            if (self.parents('#fast_form').length) {
                                if (self.parents('.second_line').length) {
                                    self.siblings('i.error').css({
                                        'top': self.parent().position().top - 30
                                    });
                                } else {
                                    self.siblings('i.error').css({
                                        'top': self.parent().position().top - 34
                                    });
                                }
                            }
                            if (self.parents('.calc_easy').length) {
                                self.siblings('i.error').css({
                                    'top': self.parent().position().top - 30
                                });
                            }
                            if (self.parents('.user_info').length) {
                                self.siblings('i.error').css({
                                    'top': self.parent().position().top - 16
                                });
                            }
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
                                error_text = 'Минимальный тираж 500 карт';
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
                //console.log(valid);
            });
            $this.find('input.for_valid').on("input", function() {
                var self = $(this),
                    pattern,
                    error_text,
                    self_name = $(this).attr('name'),
                    self_val = $(this).val();

                function add_mes() {
                    if (self.siblings('i').length == 0) {
                        self.parent().append('<i class="error">' + error_text + '</i>');
                        self.siblings('i.error').css({
                            'left': self.parent().position().left
                        });
                        if (self.parents('#easy_form').length) {
                            self.siblings('i.error').css({
                                'top': self.parent().position().top - 12
                            });
                        }
                        if (self.parents('#fast_form').length) {

                            if (self.parents('.second_line').length) {
                                self.siblings('i.error').css({
                                    'top': self.parent().position().top - 30
                                });
                            } else {
                                self.siblings('i.error').css({
                                    'top': self.parent().position().top - 34
                                });
                            }
                        }
                        if (self.parents('.calc_easy').length) {
                            self.siblings('i.error').css({
                                'top': self.parent().position().top - 30
                            });
                        }
                        if (self.parents('.user_info').length) {
                            self.siblings('i.error').css({
                                'top': self.parent().position().top - 16
                            });
                        }
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