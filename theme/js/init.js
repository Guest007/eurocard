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
		z=0;
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
	$('section.location > div > ul > li').not('current').click(function(){
		var this_id = $(this).attr('id');
		$(this).addClass('current').siblings('li').removeClass('current');
		$('section.location > div > span[rel="'+this_id+'"], section.location > span > span[rel="'+this_id+'"]')
		.addClass('current')
		.siblings('span')
		.removeClass('current');
	});
	$('section.location > div > ul > li').click(function(){
		$('section.location > div:first-child').toggleClass('drop');
		$(this).prependTo($(this).parent()[0])
	});

	//Переключатели в форме заказа
	$('div.easy_form > form > ul > li > span, div.easy_form > form > ul > li > small').not('sum').click(function(){
		var self = $(this);
		self.toggleClass('active')
		if(self.hasClass('active')){
			self.children('i').removeClass('fa-times').addClass('fa-check');
		}
		else{
			if(self.children('i').hasClass('fa-check')){
				self.children('i').removeClass('fa-check').addClass('fa-times');
			}
		}
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


});
//Глобальная загрузка Jclever для ajax контента
//$(document).ajaxComplete(function(event, xhr, settings){
		//$('.jClever').jClever({
			//selfClass: "alice",
			//applyTo: {
				//input: false,
				//select: true,
				//checkbox: true,
				//radio: true,
				//button: false,
				//file: true,
				//textarea: false
			//}
		//});
//});
