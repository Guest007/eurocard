function MP_init(objects, enable_gallery) {
    var set = $(objects);
    set.magnificPopup({
        type: 'image',
        removalDelay: 300,
        tLoading: '<div class="preloader_box"><img src="/images/modules/preloader_white.gif"></div>',
        closeMarkup: '<button title="%title%" type="button" class="mfp-close">&#xf00d;</button>',
        closeOnBgClick: true,
        closeOnContentClick: true,
        gallery: {
            enabled: enable_gallery,
            preload: [0, 0],
            arrowMarkup: '<button title="%title%" type="button" class="mfp-arrow mfp-arrow-%dir% "><span><i class="fa fa-chevron-%dir%"></i></span></button>'
        },
        callbacks: {
            beforeOpen: function() {
                this.st.image.markup = this.st.image.markup.replace('mfp-figure', 'mfp-figure mfp-with-anim');
                this.st.mainClass = this.st.el.attr('data-effect');
            },
            imageLoadComplete: function() {
                var self = this;
                setTimeout(function() {
                    self.wrap.addClass('mfp-image-loaded');
                }, 16);
            },
            buildControls: set.size() == 1 || enable_gallery == false ? function() {} : function() {
                this.contentContainer.append(this.arrowLeft.add(this.arrowRight));
            },
            close: function() {
                this.wrap.removeClass('mfp-image-loaded');
            },
            beforeClose: function() {
                $('.mfp-content .mfp-arrow').remove();
            }
        },
    });
};

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
                $('.tooltip.top').each(function() {
                    var self_height = $(this).outerHeight();
                    //console.log(self_height);
                    $(this).css({
                        'top': -(self_height + 10)
                    });
                });
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
    $('.location > div > a.call_back').click(function() {
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
/*
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
    $('div.contacts > div > div.map').each(function() {
        z++;
        $(this).attr('rel', z);
    });
    $('div.contacts > div > span > a').not('current').click(function() {
        var this_rel = $(this).attr('rel');
        $(this).addClass('current').siblings().removeClass('current');
        $('div.contacts > div > ul[rel="' + this_rel + '"], div.contacts > div > div[rel="' + this_rel + '"]').addClass('current').siblings().removeClass('current');
        return false;
    });
}
*/
/*
function back_button() {
    var path = window.location.pathname,
        part = path.split('/'),
        end_of_line = part[3],
        url = path.replace('/' + end_of_line, '.html'),
        previous = document.referrer,
        need_part = previous.split('/'),
        search_part = need_part[3],
        go_go = need_part[5];

    $('a.adress').click(function() {
        var this_url = $(this).attr('href');
        console.log(this_url);
    });
    console.log(path);
    console.log(previous);
    console.log(search_part);
    console.log(end_of_line);
    console.log(go_go);
    if (previous == '') {
        $('.go_back').attr('href', url).text('РќР°Р·Р°Рґ РІ РєР°С‚Р°Р»РѕРі');
    } else {
        if (search_part == 'catalog') {
            //var gogo
            if (go_go) {
                $('.go_back').attr('href', url).text('РќР°Р·Р°Рґ РІ РєР°С‚Р°Р»РѕРі');
            } else {
                $('.go_back').attr('href', previous).text('РќР°Р·Р°Рґ РІ РєР°С‚Р°Р»РѕРі');
            }
        } else {
            $('.go_back').attr('href', url).text('РќР°Р·Р°Рґ РІ РєР°С‚Р°Р»РѕРі');
        }
    }
}
*/

$(document).ready(function() {

    index_tabs();

    news_title_height();

    call_();



    //back_button();

    $.each(['a[rel="kool"]'], function(index, value) {
        MP_init(value, false);
    });




    var
    x = 0,
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
    $('div.contacts > div > div.map').each(function() {
        z++;
        $(this).attr('rel', z);
    });
    //$.removeCookie('city');
    $('a.adress').click(function() {
        $.removeCookie('city');
        var this_rel = $(this).attr('rel');
        $.cookie('city', this_rel);
    });

    //console.log($.cookie('city'));
    $('div.contacts > div > span > a[rel="' + $.cookie('city') + '"]').addClass('current').siblings().removeClass('current');
    $('div.contacts > div > ul[rel="' + $.cookie('city') + '"], div.contacts > div > div[rel="' + $.cookie('city') + '"]').addClass('current').siblings().removeClass('current');




    $('div.contacts > div > span > a').not('current').click(function() {
        var this_rel = $(this).attr('rel');
        $(this).addClass('current').siblings().removeClass('current');
        $('div.contacts > div > ul[rel="' + this_rel + '"], div.contacts > div > div[rel="' + this_rel + '"]').addClass('current').siblings().removeClass('current');
        return false;
    });

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
                    window.location.href = "/page/fast";
                    //$('.data_checking').addClass('thanks').html('<span>Спасибо за ваш заказ.<small class="close_order reset"><i class="fa fa-times"></i></small></span><span>Письмо с информацией отправлено на указанный вами адрес электронной почты.</span><span>В ближайшее время наш сотрудник свяжется с вами для уточнения деталей.</span>');
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

//загрузка Jclever для ajax контента
$(document).ajaxComplete(function(event, xhr, settings) {
    form_style();
});