/*!
 * timepicker.js - v2.2.0
 * A lightweight, customizable, TimePicker. Zero dependencies.
 * https://github.com/jonataswalker/timepicker.js
 * Built: Sat Jan 28 2017 15:26:36 GMT-0200 (BRST)
 */
!function (e, t) {
  'object' == typeof exports && 'undefined' != typeof module ? module.exports = t()  : 'function' == typeof define && define.amd ? define(t)  : e.TimePicker = t()
}(this, function () {
  'use strict';
  var e = '_jw-tpk',
  t = '250px',
  n = '140px',
  i = '-container',
  s = '-header',
  r = '-body',
  o = '-hour',
  a = '-minute',
  l = '-selected',
  c = '-dragging',
  u = {
    hour: 'data-hour',
    minute: 'data-minute'
  },
  d = {
    hour_list: 'hour_list_id',
    minute_list: 'minute_list_id'
  },
  h = {
    namespace: e,
    width: t,
    height: n,
    container_class: i,
    header_class: s,
    body_class: r,
    hour_class: o,
    minute_class: a,
    selected_class: l,
    dragging_class: c,
    attr: u,
    ids: d
  },
  f = Object.freeze({
    namespace: e,
    width: t,
    height: n,
    container_class: i,
    header_class: s,
    body_class: r,
    hour_class: o,
    minute_class: a,
    selected_class: l,
    dragging_class: c,
    attr: u,
    ids: d,
  default:
    h
  }),
  m = {
    open: 'open',
    close: 'close',
    change: 'change',
    start_fade_in: 'start-fade-in',
    end_fade_in: 'end-fade-in',
    start_fade_out: 'start-fade-out',
    end_fade_out: 'end-fade-out'
  },
  p = {
    lang: 'en',
    theme: 'dark'
  },
  v = {
    en: {
      hour: 'Hour',
      minute: 'Minute'
    },
    pt: {
      hour: 'Hora',
      minute: 'Minuto'
    }
  },
  g = f,
  _ = {
    container: e + i,
    header: e + s,
    body: e + r,
    hour: e + o,
    minute: e + a,
    selected: e + l,
    dragging: e + c
  },
  y = {
    focusable: /^(?:input|select|textarea|button|object)$/i,
    clickable: /^(?:a|area)$/i,
    classRegex: function (e) {
      return new RegExp('(^|\\s+) ' + e + ' (\\s+|$)')
    },
    addClass: function (e, t, n) {
      var i = this;
      if (Array.isArray(e)) return void e.forEach(function (e) {
        i.addClass(e, t)
      });
      for (var s = Array.isArray(t) ? t : t.split(/\s+/), r = s.length; r--; ) i.hasClass(e, s[r]) || i._addClass(e, s[r], n)
    },
    _addClass: function (e, t, n) {
      var i = this;
      e.classList ? e.classList.add(t)  : e.className = (e.className + ' ' + t).trim(),
      n && this.isNumeric(n) && window.setTimeout(function () {
        i._removeClass(e, t)
      }, n)
    },
    removeClass: function (e, t, n) {
      var i = this;
      if (Array.isArray(e)) return void e.forEach(function (e) {
        i.removeClass(e, t, n)
      });
      for (var s = Array.isArray(t) ? t : t.split(/\s+/), r = s.length; r--; ) i.hasClass(e, s[r]) && i._removeClass(e, s[r], n)
    },
    _removeClass: function (e, t, n) {
      var i = this;
      e.classList ? e.classList.remove(t)  : e.className = e.className.replace(this.classRegex(t), ' ').trim(),
      n && this.isNumeric(n) && window.setTimeout(function () {
        i._addClass(e, t)
      }, n)
    },
    hasClass: function (e, t) {
      return e.classList ? e.classList.contains(t)  : this.classRegex(t).test(e.className)
    },
    toggleClass: function (e, t) {
      var n = this;
      return Array.isArray(e) ? void e.forEach(function (e) {
        n.toggleClass(e, t)
      })  : void (e.classList ? e.classList.toggle(t)  : this.hasClass(e, t) ? this._removeClass(e, t)  : this._addClass(e, t))
    },
    $: function (e) {
      return e = '#' === e[0] ? e.substr(1, e.length)  : e,
      document.getElementById(e)
    },
    isElement: function (e) {
      return 'HTMLElement' in window ? !!e && e instanceof HTMLElement : !!e && 'object' == typeof e && 1 === e.nodeType && !!e.nodeName
    },
    getAllChildren: function (e, t) {
      return [].slice.call(e.getElementsByTagName(t))
    },
    getMaxZIndex: function (e, t, n) {
      void 0 === t && (t = 0),
      void 0 === n && (n = - 1);
      for (var i = this.find('*', document, !0), s = i.length; ++n < s; ) e = parseInt(window.getComputedStyle(i[n]).zIndex, 10),
      t = e ? Math.max(t, e)  : t;
      return t
    },
    mergeOptions: function (e, t) {
      var n = {
      };
      for (var i in e) n[i] = e[i];
      for (var s in t) n[s] = t[s];
      return n
    },
    createElement: function (e, t) {
      var n;
      if (Array.isArray(e)) {
        if (n = document.createElement(e[0]), e[1].id && (n.id = e[1].id), e[1].classname && (n.className = e[1].classname), e[1].attr) {
          var i = e[1].attr;
          if (Array.isArray(i)) for (var s = - 1; ++s < i.length; ) n.setAttribute(i[s].name, i[s].value);
           else n.setAttribute(i.name, i.value)
        }
      } else n = document.createElement(e);
      n.innerHTML = t;
      for (var r = document.createDocumentFragment(); n.childNodes[0]; ) r.appendChild(n.childNodes[0]);
      return n.appendChild(r),
      n
    },
    find: function (e, t, n) {
      var i = /^(#?[\w-]+|\.[\w-.]+)$/,
      s = /\./g,
      r = [
      ].slice,
      o = [
      ];
      if (i.test(e)) switch (e[0]) {
        case '#':
          o = [
            this.$(e.substr(1))
          ];
          break;
        case '.':
          o = r.call(t.getElementsByClassName(e.substr(1).replace(s, ' ')));
          break;
        default:
          o = r.call(t.getElementsByTagName(e))
      } else o = r.call(t.querySelectorAll(e));
      return n ? o : o[0]
    },
    offset: function (e) {
      var t = e.getBoundingClientRect(),
      n = document.documentElement;
      return {
        left: t.left + window.pageXOffset - n.clientLeft,
        top: t.top + window.pageYOffset - n.clientTop,
        width: e.offsetWidth,
        height: e.offsetHeight
      }
    },
    getWindowSize: function () {
      return {
        width: window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth,
        height: window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight
      }
    },
    evaluate: function (e) {
      var t;
      switch (this.toType(e)) {
        case 'window':
        case 'htmldocument':
        case 'element':
          t = e;
          break;
        case 'string':
          t = this.$(e);
          break;
        default:
          console.warn('Unknown type')
      }
      return this.assert(t, 'Can\'t evaluate: @param ' + e),
      t
    },
    toType: function (e) {
      return e === window && e.document && e.location ? 'window' : e === document ? 'htmldocument' : 'string' == typeof e ? 'string' : this.isElement(e) ? 'element' : void 0
    },
    typeOf: function (e) {
      return {
      }.toString.call(e).match(/\s([a-zA-Z]+)/) [1].toLowerCase()
    },
    events: function () {
      var e = {
      },
      t = e.hasOwnProperty;
      return {
        subscribe: function (n, i) {
          t.call(e, n) || (e[n] = [
          ]);
          var s = e[n].push(i) - 1;
          return {
            remove: function () {
              delete e[n][s]
            }
          }
        },
        publish: function (n, i) {
          t.call(e, n) && e[n].forEach(function (e) {
            e(void 0 !== i ? i : {
            })
          })
        }
      }
    },
    fade: function (e, t, n, i) {
      void 0 === n && (n = 300),
      void 0 === i && (i = 'in');
      var s,
      r,
      o = null,
      a = !1,
      l = 'in' === i ? m.start_fade_in : m.start_fade_out,
      c = 'in' === i ? m.end_fade_in : m.end_fade_out,
      u = function (d) {
        o || (e.publish(l, {
          target: t
        }), o = d),
        'in' === i ? (s = + t.style.opacity + (d - o) / n, a = s >= 1)  : (s = + t.style.opacity - (d - o) / n, a = s <= 0),
        t.style.opacity = s,
        a ? e.publish(c, {
          target: t
        })  : r = window.requestAnimationFrame(u)
      };
      return r = window.requestAnimationFrame(u)
    },
    assert: function (e, t) {
      if (!e) {
        if (t = t || 'Assertion failed', 'undefined' != typeof Error) throw new Error(t);
        throw t
      }
    }
  },
  w = function (e) {
    this.Base = e
  };
  w.prototype.createPicker = function () {
    for (var e, t, n = this.Base.options, i = w.picker.indexOf(w.replace.hour_list), s = w.picker.indexOf(w.replace.minute_list), r = w.picker.indexOf(w.replace.hour_title), o = w.picker.indexOf(w.replace.minute_title), a = [
    ], l = [
    ], c = 0, u = 6, d = 0; d < 4; d++) {
      for (t = c + u, a.push('<ol>'); c < t; c++) a.push(['<li><a ',
      g.attr.hour,
      '="',
      c,
      '">',
      c,
      '</a></li>'].join(''));
      a.push('</ol>')
    }
    for (c = 0, t = 0, u = 10, d = 0; d < 3; d++) {
      for (t = c + u, l.push('<ol>'); c < t; c += 20) e = c < 10 ? e = '0' + c : c,
      l.push(['<li><a ',
      g.attr.minute,
      '="',
      e,
      '">',
      e,
      '</a></li>'].join(''));
      l.push('</ol>')
    }
    w.picker[i] = a.join(''),
    w.picker[s] = l.join(''),
    w.picker[r] = v[n.lang].hour,
    w.picker[o] = v[n.lang].minute;
    var h = y.createElement(['div',
    {
      classname: _.container + ' ' + g.namespace + '-' + n.theme
    }
    ], w.picker.join(''));
    h.style.zIndex = y.getMaxZIndex() + 10,
    h.style.visibility = 'hidden',
    document.body.appendChild(h);
    var f = y.offset(h);
    return this.Base.container = {
      size: {
        width: f.width,
        height: f.height
      },
      element: h,
      drag_handle: h.querySelector('.' + _.header)
    },
    h.style.visibility = '',
    h.style.display = 'none',
    h
  },
  w.replace = {
    hour_list: '__hour-list__',
    minute_list: '__minute-list__',
    hour_title: '__hour-title__',
    minute_title: '__minute-title__'
  },
  w.picker = [
    '<div class="' + _.header + '">',
    '<div class="' + _.hour + '">',
    w.replace.hour_title,
    '</div>',
    '<div class="' + _.minute + '">',
    w.replace.minute_title,
    '</div>',
    '</div>',
    '<div class="' + _.body + '">',
    '<div id="' + g.ids.hour_list + '" class="' + _.hour + '">',
    w.replace.hour_list,
    '</div>',
    '<div id="' + g.ids.minute_list + '" class="' + _.minute + '">',
    w.replace.minute_list,
    '</div>',
    '</div>'
  ];
  var E = function (e) {
    var t,
    n,
    i,
    s,
    r,
    o,
    a = e.container.element,
    l = {
    },
    c = function (e) {
      e.preventDefault && e.preventDefault(),
      i = parseInt(a.style.left, 10) || 0,
      s = parseInt(a.style.top, 10) || 0,
      r = i + (e.clientX - t),
      o = s + (e.clientY - n),
      l.move.call(void 0, {
        target: a,
        x: r,
        y: o
      }),
      t = e.clientX,
      n = e.clientY
    },
    u = function () {
      document.removeEventListener('mousemove', c, !1),
      document.removeEventListener('mouseup', stop, !1),
      l.end.call(void 0, {
        target: a,
        x: r,
        y: o
      })
    },
    d = function (e) {
      0 === e.button && (t = e.clientX, n = e.clientY, l.start.call({
        target: a
      }), document.addEventListener('mousemove', c, !1), document.addEventListener('mouseup', u, !1))
    };
    return e.container.drag_handle.addEventListener('mousedown', d, !1),
    {
      when: function (e) {
        l.start = e.start,
        l.move = e.move,
        l.end = e.end
      }
    }
  },
  b = function (e) {
    this.Base = e,
    this.container = e.container.element,
    this.closeWhen = {
      hour: !1,
      minute: !1
    },
    this._ids = 0,
    this.id_active = void 0,
    this.opened = !1,
    this.targets = [
    ],
    this.collection = {
      hours: [
      ],
      minutes: [
      ]
    },
    this.events = y.events(),
    this.request_ani_id = void 0
  };
  b.prototype.init = function () {
    this.setFocusListener(this.Base.target),
    this.setSelectListener()
  },
  b.prototype.show = function (e) {
    var t = this.targets[e].element,
    n = y.offset(t),
    i = this.Base.container.size,
    s = n.top + n.height + 5,
    r = y.getWindowSize();
    n.left + i.width > r.width ? (this.container.style.left = '', this.container.style.right = '5px')  : (this.container.style.right = '', this.container.style.left = n.left + 'px'),
    n.top + i.height > r.height ? this.container.style.bottom = '5px' : this.container.style.top = s + 'px',
    this.events.subscribe(m.start_fade_in, function (e) {
      e.target.style.opacity = 0,
      e.target.style.display = 'block'
    }),
    this.request_ani_id = y.fade(this.events, this.container, 400),
    this.Base.dispatchEvent(m.open, {
      element: t
    }),
    this.handleOpen(e)
  },
  b.prototype.show_ = function () {
    var e = this;
    this.targets.forEach(function (t) {
      e.show(t.element._id)
    })
  },
  b.prototype.hide = function (e) {
    this.opened = !1,
    this.events.subscribe(m.start_fade_out, function (e) {
      e.target.style.opacity = 1,
      e.target.style.display = 'block'
    }),
    this.events.subscribe(m.end_fade_out, function (e) {
      e.target.style.display = 'none'
    }),
    this.request_ani_id = y.fade(this.events, this.container, 800, 'out'),
    this.Base.dispatchEvent(m.close, {
      element: this.targets[e].element
    })
  },
  b.prototype.hide_ = function () {
    var e = this;
    this.targets.forEach(function (t) {
      e.hide(t.element._id)
    })
  },
  b.prototype.handleOpen = function (e) {
    var t,
    n = this,
    i = this,
    s = this.targets[e].hour,
    r = this.targets[e].minute;
    y.removeClass(this.collection.hours, _.selected),
    y.removeClass(this.collection.minutes, _.selected),
    s && r && (this.collection.hours.forEach(function (e) {
      if (t = n.getHour(e), t === s) return void y.addClass(e, _.selected)
    }), this.collection.minutes.forEach(function (e) {
      if (t = n.getMinute(e), t === r) return void y.addClass(e, _.selected)
    })),
    document.addEventListener('mousedown', {
      handleEvent: function (t) {
        if (!i.container.contains(t.target)) {
          var n = !1;
          i.targets.forEach(function (e) {
            e.element === t.target && (n = !0)
          }),
          !n && i.opened && i.hide(e),
          i.targets[e].element !== t.target && document.removeEventListener(t.type, this, !1)
        }
      }
    }, !1),
    this.opened = !0,
    this.id_active = e,
    this.closeWhen = {
      hour: !1,
      minute: !1
    }
  },
  b.prototype.handleClose = function (e) {
    this.closeWhen.hour && this.closeWhen.minute && this.hide(e)
  },
  b.prototype.getHour = function (e) {
    return e.getAttribute(g.attr.hour)
  },
  b.prototype.getMinute = function (e) {
    return e.getAttribute(g.attr.minute)
  },
  b.prototype.setSelectListener = function () {
    var e = this,
    t = y.$(g.ids.hour_list),
    n = y.$(g.ids.minute_list),
    i = function (t) {
      t.preventDefault();
      var n = e.targets[e.id_active];
      n.hour = e.getHour(t.target),
      e.Base.dispatchEvent(m.change, {
        element: n.element,
        hour: n.hour,
        minute: n.minute
      }),
      y.removeClass(e.collection.hours, _.selected),
      y.addClass(t.target, _.selected),
      e.closeWhen.hour = !0,
      e.handleClose(e.id_active)
    },
    s = function (t) {
      t.preventDefault();
      var n = e.targets[e.id_active];
      n.minute = e.getMinute(t.target),
      e.Base.dispatchEvent(m.change, {
        element: n.element,
        hour: n.hour,
        minute: n.minute
      }),
      y.removeClass(e.collection.minutes, _.selected),
      y.addClass(t.target, _.selected),
      e.closeWhen.minute = !0,
      e.handleClose(e.id_active)
    };
    this.collection.hours = y.getAllChildren(t, 'a'),
    this.collection.minutes = y.getAllChildren(n, 'a'),
    this.collection.hours.forEach(function (e) {
      e.addEventListener('click', i)
    }),
    this.collection.minutes.forEach(function (e) {
      e.addEventListener('click', s)
    })
  },
  b.prototype.setFocusListener = function (e) {
    var t,
    n = this,
    i = function (e) {
      e.preventDefault(),
      window.cancelAnimationFrame(n.request_ani_id),
      n.show(e.target._id)
    },
    s = [
    ];
    e = Array.isArray(e) ? e : [
      e
    ],
    Array.prototype.push.apply(s, e),
    s.forEach(function (e) {
      if (t = y.evaluate(e)) {
        var s = n._ids++;
        t._id = s,
        n.targets[s] = {
          element: t
        },
        y.focusable.test(t.nodeName) ? t.addEventListener('focus', i, !0)  : y.clickable.test(t.nodeName) && t.addEventListener('click', i, !0)
      }
    })
  };
  var C = function () {
    this._events = this._events || {
    },
    this._onceEvents = this._onceEvents || {
    }
  };
  C.prototype.on = function (e, t) {
    if (e && t) {
      var n = this._events[e] = this._events[e] || [
      ];
      return n.indexOf(t) === - 1 && n.push(t),
      this
    }
  },
  C.prototype.once = function (e, t) {
    if (e && t) {
      this.on(e, t);
      var n = this._onceEvents[e] = this._onceEvents[e] || {
      };
      return n[t] = !0,
      this
    }
  },
  C.prototype.off = function (e, t) {
    var n = this._events && this._events[e];
    if (n && n.length) {
      var i = n.indexOf(t);
      return i !== - 1 && n.splice(i, 1),
      this
    }
  },
  C.prototype.dispatchEvent = function (e, t) {
    var n = this;
    void 0 === t && (t = {
    });
    var i = this._events && this._events[e];
    if (i && i.length) {
      for (var s = 0, r = i[s], o = this._onceEvents && this._onceEvents[e]; r; ) {
        var a = o && o[r];
        a && (n.off(e, r), delete o[r]),
        r.call(n, t),
        s += a ? 0 : 1,
        r = i[s]
      }
      return this
    }
  };
  var A = function (t) {
    function n(i, s) {
      void 0 === s && (s = {
      }),
      y.assert(Array.isArray(i) || 'string' === y.typeOf(i) || y.isElement(i), '`target` should be Element, <Array>Element, String or <Array>String.'),
      t.call(this),
      this.options = y.mergeOptions(p, s),
      this.target = i,
      this.container = {
      };
      var r = new w(this),
      o = r.createPicker(),
      a = new E(this);
      n.Internal = new b(this),
      n.Internal.init(),
      a.when({
        start: function () {
          y.addClass(o, e + c)
        },
        move: function (e) {
          o.style.left = e.x + 'px',
          o.style.top = e.y + 'px'
        },
        end: function (t) {
          y.removeClass(o, e + c),
          t.y < 0 && (o.style.top = 0)
        }
      })
    }
    return t && (n.__proto__ = t),
    n.prototype = Object.create(t && t.prototype),
    n.prototype.constructor = n,
    n.prototype.show = function () {
      n.Internal.show_()
    },
    n.prototype.hide = function () {
      n.Internal.hide_()
    },
    n.prototype.setTarget = function (e) {
      y.assert(Array.isArray(e) || 'string' === y.typeOf(e) || y.isElement(e), '`target` should be Element, <Array>Element, String or <Array>String.'),
      this.target = e,
      n.Internal.setFocusListener(this.target)
    },
    n
  }(C);
  return A
});
