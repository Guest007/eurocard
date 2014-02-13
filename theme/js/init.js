$(document).ready(function(){

	//Формы
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
	});
	$('section.order > div > ul > li').not('current').click(function(){
		var this_id = $(this).attr('id');
		$(this).addClass('current').siblings('li').removeClass('current');
		$('section.order > div > div[rel="'+this_id+'"]')
		.addClass('current')
		.siblings('div')
		.removeClass('current');
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

	//Заказ (закрываем модальное окно)
	$(document).on('click', '.close_order', function(){
		$('div.data_checking, div.overlay').remove();
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

	//Картинки в контенте

	//$('div.content > div.images').each(function(){
		var next = $(this).find('a.next'),
			prev = $(this).find('a.prev');
		$(this).children('div.carousel').carouFredSel({
			circular: false,
			infinite: false,
			items: 3,
			auto    : false,
			direction: "left",
			width: 924,
			height: 280,
			align: "left",
			prev    : {
				button  : prev,
				key     : "left"
			},
			next    : {
				button  : next,
				key     : "right"
			},
		});
	//});
	
	//Подсказки в первой форме
	$('div.easy_form > form > ul > li > small').click(function(){
			$(this).toggleClass('active');
	});

	//Калькулятор
	$('form.calc').each(function(){
		var self = $(this),
			min_count = 500,
			default_color_val = $('select[name="color"]').find("option:selected").data('price'),
			default_material_val = $('select[name="material"]').find("option:selected").data('price');

		//сбрасываем значения hidden
		$('input[type="hidden"]').val(0);

		//присваиваем значение по умолчанию селектам
		$('select').each(function(){
			var this_name = $(this).attr('name'),
			default_val = $(this).find("option:selected").data('price');
			$('input[name="'+this_name+'"]').val(default_val);
		})	
		//min тираж  - 500
		$('input[name="count"]').val('')
		$('input[name="count_hidden"]').val(min_count);

		//переключаем состояние атрибута, передаем значение в hidden, следим за измененнием
		$('span.flag').click(function(){
			var this_flag = $(this),
				flag_id = $(this).attr('id');
			this_flag.toggleClass('active');
			if($(this).hasClass('active')){
				$(this).children('i').removeClass('fa-times').addClass('fa-check');
				$('input[name="'+flag_id+'"]').val(parseInt($(this).data('price'))).trigger('change');	
			}
			else{
				if($(this).children('i').hasClass('fa-check')){
					$(this).children('i').removeClass('fa-check').addClass('fa-times');
				}
				$('input[name="'+flag_id+'"]').val('').trigger('change');
			}
		});

		//вводим тираж, следим за его значением (min - 500)
		$('input[name="count"]').keyup(function(){
			var count_val = parseFloat($(this).val())||0,
				this_name = $(this).attr('name');
			//error mes.
			if(count_val < 500){
				$(this).addClass('error').siblings('i').addClass('show');;
			}
			else{
				$(this).removeClass('error').siblings('i').removeClass('show');
				$('input[name="'+this_name+'_hidden"]').val(parseInt(count_val)).trigger('change');
			};
		});

		//следим за изменением значений селектов	
		$('select').change(function(){
			var this_name = $(this).attr('name'),
				this_val = $(this).find("option:selected").data('price');

			$('input[name="'+this_name+'"]').val(parseInt(this_val)).trigger('change');
		});

		//счетаем
		$('input[type="hidden"]').change(function(){
			var flag_val = 1,
				count_val = parseInt($('input[name="count_hidden"]').val()),
				color_val = parseInt($('input[name="color"]').val()),
				material_val = parseInt($('input[name="material"]').val());

			console.log(color_val);
			$('input.flag').each(function() {
				flag_val += parseInt($(this).val())||0;
			});

			sum = count_val*(flag_val+color_val+material_val);
			$('p.sum').html(sum+' руб.');
			//console.log(sum);
		});	
		
		//console.log(sum);

	});


});

//Глобальная загрузка Jclever для ajax контента
$(document).ajaxComplete(function(event, xhr, settings){
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
