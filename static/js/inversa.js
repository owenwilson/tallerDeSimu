function laplace(F, M) {
    "use strict";

    M = M || 4;
    M = Math.min(8, M);
    var v = [];

    function init(M) {
        var fac = [],
            h = [],
            i, k, tmp, sgn;

        fac.push(1);
        for (i = 1; i <= 2 * M; ++i) {
            fac.push(fac[fac.length - 1] * i);
        }

        h.push(0); // unused
        h.push(2 / fac[M - 1]);
        for (i = 2; i <= M; ++i) {
            var tmp = Math.pow(i, M) * fac[2 * i] / (fac[M - i] * fac[i] * fac[i - 1]);
            h.push(tmp);
        }

        sgn = M % 2 == 0 ? -1 : 1;
        v.push(0); // unused
        for (i = 1; i <= M * 2; ++i) {
            tmp = 0;
            for (k = Math.floor((i + 1) / 2); k <= Math.min(i, M); ++k) {
                tmp += h[k] / (fac[i - k] * fac[2 * k - i]);
            }
            tmp *= sgn;
            v.push(tmp);
            sgn *= -1;
        }
    }

    init(M);

    function evaluate(F, t) {
        var a = Math.LN2 / t,
            y = 0, i;
        for (i = 1; i <= 2 * M; ++i) {
            y += v[i] * F(i * a);
        }
        return a * y;
    }

    return function(t) {
        return evaluate(F, t);
    };
}

var resultado = laplace(0.648, 4);
console.log(resultado);