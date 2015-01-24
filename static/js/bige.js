COM.GOOGLE_DEEPMIND = COM.GOOGLE_DEEPMIND || {}, COM.GOOGLE_DEEPMIND.APP = function(a) {
    "use strict";
    var b = {
        isHomePage: "home" === a("body").attr("id")
    }, c = {
            body: "body",
            cookiesLink: "*[data-id='cookies']",
            footerDate: "body > footer .date",
            header: "body > header",
            headerLink: "body > header a",
            headerLogo: "body > header .logo",
            headerUnderlay: "body > header.underlay",
            headerOverlay: "body > header.overlay",
            hiringLink: "*[data-action='work-with-us']",
            page: "section.main-content > .page",
            pages: "header *[data-id='pages']",
            pageContent: "*[data-id='container']",
            scrollDown: ".scroll",
            scrollDownId: "*[data-id='scroll-down']",
            menuBtn: ".menuBtn"
        }, d = {
            bindHeaderLinks: function() {
                var e = a(window),
                    f = a(c.headerLink),
                    g = a(c.headerOverlay);
                b.isHomePage === !0 ? f.on("click", function(b) {
                    b.preventDefault();
                    var c, f = a(this);
                    c = "undefined" != typeof f.data("action") ? a("article[data-id='" + f.data("action") + "']") : 0, "toggle-menu" === f.data("action") ? d.bindMobileMenu() : (e.scrollTo(c, 800, {
                        easing: "swing"
                    }), g.hasClass("open") === !0 && g.removeClass("open"))
                }) : f.on("click", function(b) {
                    var c = a(this);
                    "toggle-menu" === c.data("action") && (b.preventDefault(), d.bindMobileMenu())
                })
            },
            bindHiringLink: function() {
                var b = a(c.hiringLink),
                    d = a(window);
                b.on("click", function(b) {
                    b.preventDefault();
                    var c, e = a(this);
                    c = "undefined" != typeof e.data("action") ? a("article[data-id='" + e.data("action") + "']") : 0, d.scrollTo(c, 800, {
                        easing: "swing"
                    })
                })
            },
            bindMobileMenu: function() {
                var b = a(c.headerOverlay);
                b.hasClass("open") ? b.removeClass("open") : b.addClass("open")
            },
            bindScrollButtons: function() {
                var b = a(window),
                    d = a(c.page);
                d.each(function() {
                    var d = a(this),
                        e = d.find(c.scrollDown);
                    e.on("click", function() {
                        var c = "scroll-down" === a(this).data("id") ? d.next() : 0;
                        b.scrollTo(c, 400, {
                            easing: "swing"
                        })
                    })
                })
            },
            bindScrollWheel: function() {
                function b() {
                    return function(b) {
                        var b = window.event || b,
                            c = Math.max(-1, Math.min(1, b.wheelDelta || -b.detail)),
                            d = a(window),
                            e = d.scrollTop(),
                            f = 0 > c ? 50 : -50;
                        return d.scrollTop(e + f), !1
                    }
                }
                var c = c || {};
                void 0 !== typeof document.addEventListener ? (document.addEventListener("mousewheel", b(), !1), document.addEventListener("DOMMouseScroll", b(), !1)) : c.attachEvent("onmousewheel", b())
            },
            bindWindowResize: function() {
                var b = a(window);
                b.on("resize", function() {
                    e.renderPageDimensions(), e.updatePageHeader()
                })
            },
            bindWindowScroll: function() {
                var b = a(window);
                b.on("scroll", e.updatePageHeader)
            }
        }, e = {
            hideOnMobile: function() {
                var b = function() {
                    return "ontouchstart" in window || "onmsgesturechange" in window
                };
                b() === !0 && a(c.scrollDownId).hide()
            },
            renderDate: function() {
                a(c.footerDate).html((new Date).getFullYear())
            },
            renderPageDimensions: function() {
                var d = a(c.page);
                d.each(function() {
                    var d = a(this),
                        e = d.find(c.pageContent),
                        f = d.find(c.scrollDown),
                        g = a(window);
                    b.isHomePage === !0 && (d.css({
                        height: g.innerHeight() + "px"
                    }), e.css({
                        "margin-top": (d.height() - e.height()) / 2 + "px"
                    })), f.css({
                        top: d.position().top + d.outerHeight() - f.outerHeight() + "px"
                    })
                })
            },
            showSite: function() {
                var b = a(c.body);
                b.addClass("show")
            },
            updatePageHeader: function() {
                function b() {
                    for (var b = a(window).scrollTop(), c = a(window).height(), d = a(document).height(), e = 1; e < q.length; e += 1) {
                        var f = q[e],
                            g = a("article[data-id='" + f + "']");
                        if (void 0 != g.offset()) {
                            var h = g.offset().top,
                                i = g.height();
                            b >= h - i / 3.09 && h - i / 4 + i > b ? a("a[data-action='" + f + "']").addClass("active") : a("a[data-action='" + f + "']").removeClass("active")
                        }
                    }
                    if (b + c == d && !a("nav li:last-child a").hasClass("nav-active")) {
                        var j = a(".nav-active").attr("data-action");
                        a("a[data-action='" + j + "']").removeClass("nav-active"), a("nav li:last-child a").addClass("nav-active")
                    }
                }
                var d, e, f = a(window),
                    g = a(c.header),
                    h = a(c.headerLogo),
                    i = a(c.headerUnderlay),
                    j = a(c.pages),
                    k = 640,
                    l = 70,
                    m = 64,
                    n = 200,
                    o = [640, 1026];
                i.css(f.scrollTop() >= 0 && f.scrollTop() <= n ? {
                    opacity: f.scrollTop() / 250
                } : f.scrollTop() >= 0 ? {
                    opacity: n / 250
                } : {
                    opacity: 0
                }), f.innerWidth() > k ? (f.scrollTop() >= 0 && (e = f.scrollTop() < l ? f.scrollTop() : l, d = f.scrollTop() < l ? m - f.scrollTop() / 3.125 : m - l / 3.125, j.css(f.innerWidth() < o[1] ? {
                    "padding-top": "2px"
                } : {
                    "padding-top": "0px"
                })), g.css({
                    top: -1 * e + "px"
                }), j.css({
                    "margin-top": e / 2.16 + "px"
                }), h.css({
                    height: d + "px",
                    "margin-top": e / 1.48 + "px"
                })) : (g.css({
                    top: "0px"
                }), j.css({
                    "margin-top": "0px",
                    "padding-top": "0px"
                }), h.css({
                    height: "35px",
                    "margin-top": "0px"
                }));
                for (var p = a("header *[data-id='pages'] a"), q = [], r = 0; r < p.length; r++) {
                    var s = p[r],
                        t = a(s).data("action");
                    q.push(t)
                }
                f.scrolled(b), b()
            }
        }, f = {
            initWebFonts: function(a) {
                try {
                    Typekit.load({
                        active: a
                    })
                } catch (b) {
                    a()
                }
                setTimeout(a, 3e3)
            },
            bindEvents: function() {
                d.bindWindowScroll(), d.bindWindowResize(), d.bindHeaderLinks(), d.bindHiringLink(), d.bindScrollButtons()
            },
            init: function() {
                e.renderPageDimensions(), e.updatePageHeader(), e.hideOnMobile(), f.bindEvents(), a().ready(function() {
                    f.initWebFonts(function() {
                        e.renderDate(), e.showSite()
                    })
                })
            }
        };
    return {
        init: f.init
    }
}(jQuery), COM.GOOGLE_DEEPMIND.APP.init();
//# sourceMappingURL=app.map
