(function(t){function e(e){for(var a,r,c=e[0],s=e[1],p=e[2],l=0,d=[];l<c.length;l++)r=c[l],Object.prototype.hasOwnProperty.call(o,r)&&o[r]&&d.push(o[r][0]),o[r]=0;for(a in s)Object.prototype.hasOwnProperty.call(s,a)&&(t[a]=s[a]);u&&u(e);while(d.length)d.shift()();return i.push.apply(i,p||[]),n()}function n(){for(var t,e=0;e<i.length;e++){for(var n=i[e],a=!0,c=1;c<n.length;c++){var s=n[c];0!==o[s]&&(a=!1)}a&&(i.splice(e--,1),t=r(r.s=n[0]))}return t}var a={},o={app:0},i=[];function r(e){if(a[e])return a[e].exports;var n=a[e]={i:e,l:!1,exports:{}};return t[e].call(n.exports,n,n.exports,r),n.l=!0,n.exports}r.m=t,r.c=a,r.d=function(t,e,n){r.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:n})},r.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},r.t=function(t,e){if(1&e&&(t=r(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var n=Object.create(null);if(r.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var a in t)r.d(n,a,function(e){return t[e]}.bind(null,a));return n},r.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return r.d(e,"a",e),e},r.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},r.p="/";var c=window["webpackJsonp"]=window["webpackJsonp"]||[],s=c.push.bind(c);c.push=e,c=c.slice();for(var p=0;p<c.length;p++)e(c[p]);var u=s;i.push([0,"chunk-vendors"]),n()})({0:function(t,e,n){t.exports=n("cd49")},3723:function(t,e,n){"use strict";n("c1dc")},4006:function(t,e,n){"use strict";n("95b4")},"44bc":function(t,e,n){},5843:function(t,e,n){"use strict";n("44bc")},"8d62":function(t,e,n){},"95b4":function(t,e,n){},"99e6":function(t,e,n){"use strict";n("8d62")},c1dc:function(t,e,n){},cd49:function(t,e,n){"use strict";n.r(e);n("e260"),n("e6cf"),n("cca6"),n("a79d");var a=n("7a23");function o(t,e){var n=Object(a["u"])("router-view");return Object(a["p"])(),Object(a["d"])(n)}n("4006");const i={};i.render=o;var r=i,c=n("6c02"),s=(n("9911"),n("b0c0"),n("a4d3"),n("e01a"),Object(a["e"])('<div class="body"><span class="start-message"> Integrate math with <br> Math<span class="api">API</span></span><span class="description-text"> Solve function, get function points for a plot, get derivatives and integrals, solve problems with numerical methods and much more... <br><br> With Math<span class="api">API</span> integrating math to your proyects just became easy. </span></div>',1)),p={class:"body body-info"},u=Object(a["g"])("span",{class:"description-text"},[Object(a["f"])(" With Math"),Object(a["g"])("span",{class:"api"},"API"),Object(a["f"])(" yo can ")],-1),l={class:"feature-container"},d={class:"feat-name"},b={class:"feat-description"};function h(t,e,n,o,i,r){var c=Object(a["u"])("top-bar");return Object(a["p"])(),Object(a["d"])("div",null,[Object(a["g"])(c),s,Object(a["g"])("div",p,[u,Object(a["g"])("div",l,[(Object(a["p"])(!0),Object(a["d"])(a["a"],null,Object(a["t"])(t.features,(function(e,n){return Object(a["p"])(),Object(a["d"])("div",{class:"feature-box",onClick:function(n){return t.goToDoc(e.link)},key:n},[Object(a["g"])("div",d,[Object(a["g"])("span",null,Object(a["w"])(e.name),1),Object(a["g"])("img",{class:"feat-icon",src:e.icon,alt:""},null,8,["src"])]),Object(a["g"])("div",b,[Object(a["g"])("span",null,Object(a["w"])(e.description),1)])],8,["onClick"])})),128))])])])}var f={class:"top-bar"},g=Object(a["f"])(" Math"),v=Object(a["g"])("span",{class:"api"},"API",-1),m={class:"page-buttons"};function j(t,e,n,o,i,r){return Object(a["p"])(),Object(a["d"])("div",f,[Object(a["g"])("span",{onClick:e[1]||(e[1]=function(){return t.goHome&&t.goHome.apply(t,arguments)}),class:"api-name"},[g,v]),Object(a["g"])("div",m,[Object(a["g"])("span",{onClick:e[2]||(e[2]=function(){return t.goToDocs&&t.goToDocs.apply(t,arguments)}),class:"docs-button"},"Docs"),Object(a["g"])("span",{onClick:e[3]||(e[3]=function(){return t.goToTryAPI&&t.goToTryAPI.apply(t,arguments)}),class:"try-it-button"},"Try it")])])}var y=Object(a["h"])({name:"top-bar",methods:{goToDocs:function(){window.open("https://github.com/jralvarenga/mathapi")},goToTryAPI:function(){this.$router.push("/try-api")},goHome:function(){this.$router.push("/")}}});n("5843");y.render=j;var O=y,x=Object(a["h"])({name:"Home",components:{TopBar:O},data:function(){return{features:[{name:"Function Solver",description:"Solves function in any point given, gets plot points and gets function critic values",link:"https://github.com/jralvarenga/mathapi/tree/master/mathapi/math/function",icon:"icons/function.svg"},{name:"Function Derivative",description:"Get function derivative and/or can evaluate derivatives in any point given",link:"https://github.com/jralvarenga/mathapi/tree/master/mathapi/math/derivative",icon:"icons/plot.svg"},{name:"Function Integral",description:"Get function integral and/or can evaluate integral in any point given",link:"https://github.com/jralvarenga/mathapi/tree/master/mathapi/math/integral",icon:"icons/integral.svg"},{name:"Euler Functions",description:"Returns gamma, beta & phi functions of any number",link:"https://github.com/jralvarenga/mathapi/tree/master/mathapi/math/euler_functions",icon:"icons/euler.svg"},{name:"Factorial",description:"Gets the factorial value of an integer or fraction",link:"https://github.com/jralvarenga/mathapi/tree/master/mathapi/math/factorial",icon:"icons/factorial.svg"},{name:"Algebra",description:"To be added",link:"#",icon:"icons/algebra.svg"},{name:"Geometry",description:"To be added",link:"#",icon:"icons/geometry.svg"},{name:"Numerical Methods",description:"Solves any problem with any numeric method",link:"https://github.com/jralvarenga/mathapi/tree/master/mathapi/math/methods",icon:"icons/methods.svg"}]}},methods:{goToDoc:function(t){window.open(t)}}});n("3723");x.render=h;var w=x,k={class:"try-body"},T={class:"body-request"},S=Object(a["g"])("div",{class:"title"},[Object(a["g"])("span",null,"Try the API")],-1),P=Object(a["g"])("div",{class:"description"},[Object(a["g"])("span",null,[Object(a["f"])("Select or write the API url you what to try (Read the "),Object(a["g"])("a",{target:"_blank",href:"https://github.com/jralvarenga/mathapi"},"docs"),Object(a["f"])(" first)")])],-1),A={class:"input-container"},I=Object(a["e"])('<option value="plot">Function plot</option><option value="derivative">Derivative</option><option value="integral">Integral</option><option value="beta">Beta function</option><option value="factorial">Factorial</option><option value="newton-rhapson">Newton Rhapson method</option><option value="trapz-rule">Trapezoidal rule</option>',7),J={class:"json-editor"},N={class:"body-response"};function M(t,e,n,o,i,r){var c=Object(a["u"])("top-bar");return Object(a["p"])(),Object(a["d"])("div",null,[Object(a["g"])(c),Object(a["g"])("div",k,[Object(a["g"])("div",T,[S,P,Object(a["g"])("div",A,[Object(a["A"])(Object(a["g"])("input",{class:"url-input",type:"text","onUpdate:modelValue":e[1]||(e[1]=function(e){return t.url=e})},null,512),[[a["y"],t.url]]),Object(a["g"])("select",{class:"url-select",onChange:e[2]||(e[2]=function(){return t.changeBody&&t.changeBody.apply(t,arguments)})},[I],32)]),Object(a["g"])("div",J,[Object(a["A"])(Object(a["g"])("textarea",{class:"json-textarea","onUpdate:modelValue":e[3]||(e[3]=function(e){return t.body=e})},null,512),[[a["y"],t.body]]),Object(a["g"])("button",{class:"send-button",onClick:e[4]||(e[4]=function(){return t.getResponse&&t.getResponse.apply(t,arguments)})},"Send")])]),Object(a["g"])("div",N,[Object(a["A"])(Object(a["g"])("textarea",{class:"json-textarea response-json","onUpdate:modelValue":e[5]||(e[5]=function(e){return t.response=e})},null,512),[[a["y"],t.response]])])])])}var C=n("1da1"),D=(n("96cf"),n("d3b7"),Object(a["h"])({components:{TopBar:O},name:"TryAPI",data:function(){return{url:"https://mathapi.vercel.app/api/function/points/",body:JSON.stringify({fx:"3*x^(3) + 2*x - 1",from:-1,to:5},void 0,2),response:JSON.stringify({},void 0,2)}},methods:{changeBody:function(t){var e=t.target.value;switch(e){case"plot":this.url="https://mathapi.vercel.app/api/function/points/",this.body=JSON.stringify({fx:"3*x^(3) + 2*x - 1",from:-1,to:5},void 0,2);break;case"derivative":this.url="https://mathapi.vercel.app/api/derivative/",this.body=JSON.stringify({fx:"3*x^(3) - 2*x^(1/2) + 1"},void 0,2);break;case"integral":this.url="https://mathapi.vercel.app/api/integral/",this.body=JSON.stringify({fx:"3*x^(3) - 2*x^(1/2) + 1"},void 0,2);break;case"beta":this.url="https://mathapi.vercel.app/api/euler-functions/beta/",this.body=JSON.stringify({x:"1/2",y:"3"},void 0,2);break;case"factorial":this.url="https://mathapi.vercel.app/api/factorial/",this.body=JSON.stringify({n:"1/2"},void 0,2);break;case"newton-rhapson":this.url="https://mathapi.vercel.app/api/numeric-methods/function-root/newton-rhapson/",this.body=JSON.stringify({fx:"2*x^(3)-2*x-5",xi:2},void 0,2);break;case"trapz-rule":this.url="https://mathapi.vercel.app/api/numeric-methods/integral/trapz/",this.body=JSON.stringify({fx:"3*x^(2) + 3*x - 1",a:0,b:1},void 0,2);break;default:this.url="https://mathapi.vercel.app/api/function/points/",this.body=JSON.stringify({fx:"3*x^(3) + 2*x - 1",from:-1,to:5},void 0,2);break}},getResponse:function(){var t=this;return Object(C["a"])(regeneratorRuntime.mark((function e(){var n,a,o,i;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return n=t.url,a=t.body,e.next=4,fetch(n,{method:"post",headers:{"Content-Type":"application/json"},body:a,redirect:"follow"});case 4:return o=e.sent,e.next=7,o.json();case 7:i=e.sent,t.response=JSON.stringify(i,void 0,2);case 9:case"end":return e.stop()}}),e)})))()}}}));n("99e6");D.render=M;var R=D,_=[{path:"/",name:"Home",component:w},{path:"/try-api",name:"TryAPI",component:R}],F=Object(c["a"])({history:Object(c["b"])("/"),routes:_}),B=F;Object(a["c"])(r).use(B).mount("#app")}});
//# sourceMappingURL=app.9103a88a.js.map