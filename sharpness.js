// TIP: RUN WITH node.js

// edo = 119

for (let edo = 1; edo< 118; edo++){
    var val = [2, 3].map (function (q) {return Math.round(edo * Math.log(q) / Math.LN2);});
    var fifthStep = -val[0] + val[1];
    var sharpValue = -11*val[0] + 7*val[1];

    if (sharpValue%2==0) console.log(edo, sharpValue)
}