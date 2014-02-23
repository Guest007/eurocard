    //Калькулятор

(function(){
    $.fn.calc = function(){
        return this.each(function(){

            function get_cookie(name){
                var cookie_value = null;
                if(document.cookie && document.cookie != ''){
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
                $('html').addClass('hidden');
                $('body').addClass('under_overlay')
                .append('<div class="overlay"></div><div class="data_wrap"><div><div class="data_container"><div class="data_checking"></div></div></div></div>');
                $('.data_checking').load('/second/'+result.id+'/');
            }

            if($(this).hasClass('calc')){
                var $this = $(this),
                    valid = null,
                    hidden = $(this).find('input[type="hidden"]'),
                    select = $(this).find('select'),
                    checkbox = $(this).find('input[type="checkbox"]');

                hidden.not('.ratio').val(0);
                $this.find('input[name="count"]').val('');
                $this.find('input[name="count_hidden"]').val(0);

                select.each(function(){
                    var self = $(this),
                        self_name = $(this).attr('name'),
                        self_val = $(this).find('option:selected').data('price').replace(',','.');
                    $this.find('input[name="'+self_name+'"]').val(self_val);
                });

                select.change(function(){
                    var self_name = $(this).attr('name'),
                        self_val = $(this).find('option:selected').data('price').replace(',','.');
                    $this.find('input[name="'+self_name+'"]').val(parseFloat(self_val)).trigger('change');
                });

                if($this.find('span.flag').length > 0) {
                    $('span.flag').click(function(){
                        var self = $(this),
                            self_id = $(this).attr('id');
                        self.toggleClass('active');
                        if(self.hasClass('active')){
                            self.children('i').removeClass('fa-times').addClass('fa-check');
                            $this.find('input[name="'+self_id+'"]').val(parseFloat(self.data('price').replace(',','.')));
                        }
                        else{
                            if(self.children('i').hasClass('fa-check')){
                                self.children('i').removeClass('fa-check').addClass('fa-times');
                            }
                            $this.find('input[name="'+self_id+'"]').val('0');
                        };
                        $this.find('input[name="'+self_id+'"]').trigger('change');
                    });
                    $this.find('small.question').click(function(){
                            $(this).toggleClass('active');
                    });
                }
                else {
                    checkbox.change(function(){
                        var self = $(this),
                            self_name = $(this).attr('name'),
                            //this_checked = $(this).prop('checked'),
                            self_val = $(this).data('price').replace(',','.');
                        if(self.is(':checked')){
                            $this.find('input[name="'+self_name+'"]').val(parseFloat(self_val));
                        }
                        else{
                            $this.find('input[name="'+self_name+'"]').val(0);
                        }

                    });
                }

                $this.find('input[name="count"]').keyup(function(){
                    var self = $(this),
                        self_val = parseFloat($(this).val())||0;
                    if(self_val < 500){
                        /*
                        if(self.siblings('i.error').length == 0){
                            self.addClass('error')
                            self.parent().append('<i class="error show">Минимальное значение 500 экземпляров</i>');
                            self.siblings('i.error').css({
                                'left': self.parent().position().left,
                                'top': self.parent().position().top - 36
                            });
                        }
                        */
                        $this.find('input[name="count_hidden"]').val(0).trigger('change');
                    }
                    else{
                        //self.removeClass('error').siblings('i.error').remove();
                        $this.find('input[name="count_hidden"]').val(parseFloat(self_val)).trigger('change');
                    };
                });

                if($this.find('input[type="file"]').length > 0){
                    $("#file_data").change(function() {
                        var options = {
                            url: '/uploadfile/',
                            replaceTarget: true,
                            target: $('#fd'),
                            success: function(data) {
                            }
                        };
                        $this.ajaxSubmit(options);
                    });
                }

                hidden.change(function(){
                    var flag_val = 0,
                        count_val = parseFloat($this.find('input[name="count_hidden"]').val()),
                        color_val = parseFloat($this.find('input[name="colors"]').val()),
                        material_val = parseFloat($this.find('input[name="materials"]').val()),
                        lamination_val = parseFloat($this.find('input[name="lamination"]').val()),
                        face_color = parseFloat($this.find('input[name="color_front"]').val()),
                        back_color = parseFloat($this.find('input[name="color_back"]').val()),
                        total_colors = color_val + face_color + back_color;

                    $this.find('input.flag').each(function() {
                        flag_val += parseFloat($(this).val())||0;
                    });
                    var values = {},
                        range_array =[];
                    $this.find('input.ratio').each(function() {
                        var self_val = parseFloat($(this).val().replace(',','.'));
                            self_name = parseFloat($(this).attr('name')),
                            q = count_val-self_name;
                        if(q > 0){
                            values[self_val] = q;
                            range_array.push(q);
                        } 
                    });
                    var min = Math.min.apply(null, range_array);
                    var z = 1;
                    $.each(values, function(key, value){
                        if(value == min){
                            z = parseFloat(key);
                        }              
                    });
                    var sum = parseFloat(z*count_val*(flag_val+total_colors+material_val+lamination_val)).toFixed(2);
                    $this.find('input[name="sum"]').val(sum);
                    $this.find('p.sum').html(sum+' руб.');
                });



                function validate() {
                    var validate_values = {},
                        a = [],
                        b = [];  
                    $this.find('input.for_valid').each(function(){
                        var self = $(this),
                            self_name = $(this).attr('name'),
                            self_val = $(this).val();
                            console.log(self, self_name);
                        validate_values[self_name] = self_val;
                        a.push(self_val);
                    });
                    if ($.inArray('', a) > -1 ) {
                        $.each(validate_values, function(key, value){
                            if(value == ''){
                                if($this.find('input[name="'+key+'"]').siblings('i').length == 0){
                                    $this.find('input[name="'+key+'"]').parent().append('<i class="error show">Поле не заполнено</i>');
                                    $this.find('input[name="'+key+'"]').siblings('i.error').css({
                                        'left': $this.find('input[name="'+key+'"]').parent().position().left,
                                        'top': $this.find('input[name="'+key+'"]').parent().position().top - 36
                                    });
                                    console.log($this.find('input[name="'+key+'"]').position().left, $this.find('input[name="'+key+'"]').parent().position().top);
                                }
                            }
                            else {
                                $this.find('input[name="'+key+'"]').siblings('i.error').remove();
                                    var pattern,
                                        error_text;
                                    function check_function() {
                                        if(value.match(pattern)){
                                            b.push(1);
                                            $this.find('input[name="'+key+'"]').siblings('i.error').remove();


                                        }
                                        else{
                                            b.push(0);

                                            if($this.find('input[name="'+key+'"]').siblings('i').length == 0){
                                                $this.find('input[name="'+key+'"]').parent().append('<i class="error show">'+error_text+'</i>');
                                                $this.find('input[name="'+key+'"]').siblings('i.error').css({
                                                    'left': $this.find('input[name="'+key+'"]').parent().position().left,
                                                    'top': $this.find('input[name="'+key+'"]').parent().position().top - 36
                                                });
                                                console.log($this.find('input[name="'+key+'"]').position().left, $this.find('input[name="'+key+'"]').parent().position().top);
                                            }
                                    
                                            //$this.find('i.error').addClass('show')
                                        }
                                    }
                                    if(key == 'user') {
                                        pattern = /^[a-zA-ZА-Яа-яЁё\s-]+$/;
                                        error_text = 'name_is_not_valid';
                                        check_function();

                                    }
                                    if(key == 'phone_'){
                                        pattern = /^\d+$/;
                                        error_text = 'phone_is_not_valid';
                                        check_function();
                                    }
                                    if(key == 'email'){
                                        pattern = /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,4}$/;
                                        error_text = 'email_is_not_valid';
                                        check_function();
                                    }
                            }
                        });
                    } 
                    else {
                        $.each(validate_values, function(key, value){
                            $this.find('input[name="'+key+'"]').siblings('label').removeClass('error');
                            var pattern,
                                error_text;
                            function check_function() {
                                if(value.match(pattern)){
                                    b.push(1);
                                    $this.find('input[name="'+key+'"]').siblings('i.error').remove();


                                }
                                else{
                                    b.push(0);

                                    if($this.find('input[name="'+key+'"]').siblings('i').length == 0){
                                        $this.find('input[name="'+key+'"]').parent().append('<i class="error show">'+error_text+'</i>');
                                        $this.find('input[name="'+key+'"]').siblings('i.error').css({
                                            'left': $this.find('input[name="'+key+'"]').parent().position().left,
                                            'top': $this.find('input[name="'+key+'"]').parent().position().top - 36
                                        });
                                        console.log($this.find('input[name="'+key+'"]').position().left, $this.find('input[name="'+key+'"]').parent().position().top);
                                    }
                            
                                    //$this.find('i.error').addClass('show')
                                }
                            }
                            if(key == 'user') {
                                pattern = /^[a-zA-ZА-Яа-яЁё\s-]+$/;
                                error_text = 'name_is_not_valid';
                                check_function();

                            }
                            if(key == 'phone_'){
                                pattern = /^\d+$/;
                                error_text = 'phone_is_not_valid';
                                check_function();
                            }
                            if(key == 'email'){
                                pattern = /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,4}$/;
                                error_text = 'email_is_not_valid';
                                check_function();
                            }
                        });
                        if ($.inArray(0, b) > -1 ) {
                            valid = false;
                        }
                        else{
                            valid = true;
                        }
                        //console.log(valid);
                    } 
                }

                $this.submit(function(){


                    //console.log("Call AJAX", csrftoken);
                    $this.find('input[name="csrfmiddlewaretoken"]').val(csrftoken);
                    //console.log($('#file_data'));
                    var action = $(this).attr('action'),
                        self = $(this),
                        selection = $this.find('input, select').not(' .ratio, input[name="colors"], input[name="materials"], input[name="count_hidden"], input[name="lamination"], input[name="color_front"], input[name="color_back"]').serialize();
                    //console.log(selection);
                    //console.log(action);
                    $.ajax({
                        url: action,
                        type: 'POST',
                        data: selection,
                        before_send: function(xhr, settings) {
                            //console.log("Before SENT")
                            if (!csrf_safe_method(settings.type) && same_origin(settings.url)) {
                                xhr.setRequestHeader("X-CSRFToken", csrftoken);
                            }
                        },
                        success: function(result){
                            validate();
                            //console.log(valid);
                            if(valid == true){
                                confirm_order(result);
                            } 
                        }
                    });
                    return false;
                });
            }
            else{
                $(this).children('li').each(function(){
                    $(this).find('input[type="text"]').val('').keyup(function(){
                        var one_price = parseFloat($(this).siblings('span').children('small').html()),
                            count = parseFloat($(this).val())||0,
                            total = one_price*count,
                            total_fix = total.toFixed(2);
                            //console.log(count, total, one_price);
                        if(count <= 0){
                            $(this).addClass('error').siblings('span').children('span').html('');
                        }
                        else{
                            $(this).removeClass('error').siblings('span').children('span').html(total_fix+'руб.');
                        }
                    });

                    $(this).find('form').submit(function(){


                        //console.log("Call AJAX", csrftoken);
                        $(this).find('input[name="csrfmiddlewaretoken"]').val(csrftoken);
                        //console.log($('#file_data'));
                        var action = $(this).attr('action'),
                            self = $(this),
                            selection = $this.find('input, select').not(' .ratio, input[name="colors"], input[name="materials"], input[name="count_hidden"], input[name="lamination"], input[name="color_front"], input[name="color_back"]').serialize();
                        //console.log(selection);
                        //console.log(action);
                        $.ajax({
                            url: action,
                            type: 'POST',
                            data: selection,
                            before_send: function(xhr, settings) {
                                //console.log("Before SENT")
                                if (!csrf_safe_method(settings.type) && same_origin(settings.url)) {
                                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                                }
                            },
                            success: function(result){

                                    confirm_order(result);
 
                            }
                        });
                        return false;
                    });
                });


            }


        });
    }
}());







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

$(document).ready(function(){

    //$('form.calc').calc();
    //Формы
    //form_style();

    //Выбор адреса
    var x=0,
        y=0,
        z=0,
        f=0;
    tabs_count = $('section.location > div > ul > li').length;
    $('section.location > div > ul > li').each(function(){
        x++;
        $(this).attr('id', x);
    });
    $('section.location > div > span').each(function(){
        y++;
        $(this).attr('rel', y);
    });
    $('section.location > span > span').each(function(){
        z++;
        $(this).attr('rel', z);
    });
    $('footer > div > span > span').each(function(){
        f++;
        $(this).attr('rel', f);
    });
    $('section.location > div > ul > li').not('current').click(function(){
        var this_id = $(this).attr('id');
        $(this).addClass('current').siblings('li').removeClass('current');
        $('section.location > div > span[rel="'+this_id+'"], section.location > span > span[rel="'+this_id+'"], footer > div > span > span[rel="'+this_id+'"]')
        .addClass('current')
        .siblings('span')
        .removeClass('current');
    });
    $('section.location > div > ul > li').click(function(){
        $('section.location > div:first-child').toggleClass('drop');
        $(this).prependTo($(this).parent()[0])
    });

    //Табы
    var i=0,
        h=0;
    tabs_count = $('section.order > div > ul > li').length;
    $('section.order > div > ul > li').each(function(){
        i++;
        $(this).attr('id', i);
    });
    $('section.order > div > div').each(function(){
        h++;
        $(this).attr('rel', h);

        if($(this).hasClass('current')){
            $(this).load('/form_'+h+'/', function(){
                //console.log($(this));
                $(this).children('form').calc();
                //form_style();
            });
        }
 
    });
    $('section.order > div > ul > li').not('current').click(function(){
        var this_id = $(this).attr('id'),
            form_container = $('section.order > div > div[rel="'+this_id+'"]');
        $(this).addClass('current').siblings('li').removeClass('current');
        form_container
        .addClass('current')
        .siblings('div')
        .removeClass('current');
  
        if(form_container.children('form').length == 0){
            form_container.load('/form_'+this_id+'/', function(){
                //calc();
                //form_style()
                console.log($(this));
                $(this).children('form').calc();
                $(this).children('ul').calc();
            });
        }
 
    });   

    //Расчёт стоимости
    /*
    $('.ready > ul > li').each(function(){
        $(this).find('input[type="text"]').val('').keyup(function(){
            var one_price = parseFloat($(this).siblings('span').children('small').html()),
                count = parseFloat($(this).val())||0,
                total = one_price*count,
                total_fix = total.toFixed(2);
                //console.log(count, total, one_price);
            if(count <= 0){
                $(this).addClass('error').siblings('span').children('span').html('');
            }
            else{
                $(this).removeClass('error').siblings('span').children('span').html(total_fix+'руб.');
            }
        });
    });
*/
    //Заказ (открываем модальное окно)
    /*
    $('form.filter').each(function(){
        var self=$(this);
        $('a.next_step').click(function(){
            $('body').addClass('under_overlay')
            .append('<div class="overlay"></div><div class="data_checking"><form class="jClever"></form></div>');
            $('.data_checking > form').load('/static/include/helpers.html', function(){
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
                    }
                });
            });
            return false;
        });
    });
    */
    //Заказ (закрываем модальное окно)
    $(document).on('click', '.close_order', function(){
        $('div.data_checking, div.overlay').remove();
        $('body, html').removeClass();
    });

    $(document).on('click', '.data_checking a.next_step', function(){
        $('.data_checking').find('.order').addClass('hide');
        $('.data_checking').addClass('files').find('.files').removeClass('hide');
        return false;
    });
    $(document).on('click', '.data_checking a.back', function(){
        $('.data_checking').find('.files').removeClass('hide');
        $('.data_checking').removeClass('files').find('.order').removeClass('hide');
        //$('.data_checking > form').load('/include/helpers.html .files');
        return false;
    });

    //Обратный звонок
    $('.location > a').click(function(){
        $(this).siblings('form').removeClass('hide');
        return false;
    });
    $('form.call > span > small').click(function(){
        $(this).parents('form').addClass('hide');
    });

    //Убираем слэш
    $('div.ready > ul > li').each(function(){
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

    //Подсказки в первой форме
    $('div.easy_form > form > ul > li > small').click(function(){
            $(this).toggleClass('active');
    });

    //calc();



    



});

//Глобальная загрузка Jclever для ajax контента

$(document).ajaxComplete(function(event, xhr, settings){
    form_style();
});



