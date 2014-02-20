    //Калькулятор

function calc(){
    $('form.calc').each(function(){
        //сбрасываем значения hidden
        $('input[type="hidden"]').not('.ratio').val(0);
        //присваиваем значение по умолчанию селектам
        $('select.calc').each(function(){
            var this_name = $(this).attr('name')
            default_val = $(this).find('option:selected').data('price').replace(',','.');
            //console.log(default_val);
            $('input[name="'+this_name+'"]').val(default_val);
        })
    	$('p.sum').html('0.00 руб.');
        //min тираж  - 500
        $('input[name="count"]').val('')
        $('input[name="count_hidden"]').val(0);
        //переключаем состояние атрибута, передаем значение в hidden, следим за измененнием
        $('span.flag').click(function(){
            var this_flag = $(this),
                flag_id = $(this).attr('id');
            this_flag.toggleClass('active');
            if($(this).hasClass('active')){
                $(this).children('i').removeClass('fa-times').addClass('fa-check');
                //console.log("qwertyui", parseFloat($(this).data('price')));
                $('input[name="'+flag_id+'"]').val(parseFloat($(this).data('price').replace(',','.'))).trigger('change');
            }
            else{
                if($(this).children('i').hasClass('fa-check')){
                    $(this).children('i').removeClass('fa-check').addClass('fa-times');
                }
                $('input[name="'+flag_id+'"]').val('0').trigger('change');
            }
        });
        //вводим тираж, следим за его значением (min - 500)
        $('input[name="count"]').keyup(function(){
            var count_val = parseFloat($(this).val())||0,
                this_name = $(this).attr('name');
            //error mes.
            if(count_val < 500){
                $(this).addClass('error').siblings('i').addClass('show');
                $('input[name="count_hidden"]').val(0);
            }
            else{
                $(this).removeClass('error').siblings('i').removeClass('show');
                $('input[name="'+this_name+'_hidden"]').val(parseFloat(count_val)).trigger('change');
            };
        });
        //следим за изменением значений селектов
        $('select').change(function(){
            var this_name = $(this).attr('name'),
                this_val = $(this).find("option:selected").data('price').replace(',','.');

            $('input[name="'+this_name+'"]').val(parseFloat(this_val)).trigger('change');
        });

        $('input[type="checkbox"]').change(function(){
        	var this_name = $(this).attr('name'),
        		this_checked = $(this).prop('checked'),
        		this_val = $(this).data('price').replace(',','.');
        	if($(this).is(':checked')){
        		$('input[name="'+this_name+'"]').val(parseFloat(this_val));
        	}
        	else{
        		$('input[name="'+this_name+'"]').val(0);
        	}
        	$('input[type="hidden"]').trigger('change');
        });
        //счетаем
        $('input[type="hidden"]').change(function(){
            var flag_val = 0,
                count_val = parseFloat($('input[name="count_hidden"]').val()),
                color_val = parseFloat($('input[name="colors"]').val()),
                material_val = parseFloat($('input[name="materials"]').val()),
                lamination_val = parseFloat($('input[name="lamination"]').val()),
                face_color = parseFloat($('input[name="color_front"]').val()),
                back_color = parseFloat($('input[name="color_back"]').val()),
                total_colors = color_val + face_color + back_color;
            $('input.flag').each(function() {
                flag_val += parseFloat($(this).val())||0;
            });
            var values = {},
                range_array =[];
            $('input.ratio').each(function() {
                var this_val = parseFloat($(this).val().replace(',','.'));
                    this_name = parseFloat($(this).attr('name')),
                    q = count_val-this_name;
                if(q > 0){
                    values[this_val] = q;
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
            $('input[name="sum"]').val(sum);
            $('p.sum').html(sum+' руб.');
        });
        function get_cookie(name){
            var cookie_value = null;
            if(document.cookie && document.cookie != ''){
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookie_value = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookie_value;
        };
        var csrftoken = get_cookie('csrftoken');
        function csrf_safe_method(method) {
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        };
        function same_origin(url) {
            var host = document.location.host; // host + port
            var protocol = document.location.protocol;
            var sr_origin = '//' + host;
            var origin = protocol + sr_origin;
            // Allow absolute or scheme relative URLs to same origin
            return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
                (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
                // or any other URL that isn't scheme relative or absolute i.e relative.
                !(/^(\/\/|http:|https:).*/.test(url));
        };
        /*
        $.ajaxSetup({
            before_send: function(xhr, settings) {
                console.log("Before SENT")
                if (!csrf_safe_method(settings.type) && sameOrigin(settings.url)) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });
        */
        $(this).submit(function(){
            console.log("Call AJAX", csrftoken);
            $('input[name="csrfmiddlewaretoken"]').val(csrftoken);
            console.log($('#file_data'));
            var action = $(this).attr('action'),
            	self = $(this),
            	selection = $(this).find('input, select').not(' .ratio, input[name="colors"], input[name="materials"], input[name="count_hidden"], input[name="lamination"], input[name="color_front"], input[name="color_back"]').serialize();
            console.log(selection);
            console.log(action);
            $.ajax({
                url: action,
                type: 'POST',
                data: selection,
                before_send: function(xhr, settings) {
                    console.log("Before SENT")
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
        
        //Заказ (открываем модальное окно)
        function confirm_order(result) {
            $('input#id').val(result.id);
            $('html').addClass('hidden');
            $('body').addClass('under_overlay')
            .append('<div class="overlay"></div><div class="data_wrap"><div><div class="data_container"><div class="data_checking"><form class="jClever"></form></div></div></div></div>');
            $('.data_checking > form').load('/second/'+result.id+'/'
                , function(){
                form_style()
            }
            
            );
        }
    });
}

function validate() {
     var method = {
        numeric: function(data) {
            var pattern = /^\d+$/;
            return pattern.test(data);
        },
        string: function(data) {
            var pattern = /^[a-zA-ZА-Яа-я]+$/;
            return pattern.test(data);
        },
        text: function(data) {
            var pattern = /^[a-zA-ZА-Яа-я0-9]+$/;
            return pattern.test(data);
        },
        email: function(data) {
            var pattern = /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,4}$/;
            return pattern.test(data);
        },
        url: function(data) {
            var pattern = /^((https?|ftp)\:\/\/)?([a-z0-9]{1,})([a-z0-9-.]*)\.([a-z]{2,4})$/;
            return pattern.test(data);
        }

    };
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

$(document).ready(function(){

	//Формы
	form_style();

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
            	calc();
            	form_style()
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
            	calc();
            	form_style()
            });
        }
 
    });   

	//Расчёт стоимости
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

//$(document).ajaxComplete(function(event, xhr, settings){
	//calc();
	//form_style();
//});



