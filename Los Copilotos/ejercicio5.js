function ejercicio5(dividend, divisor) {

    let quotient = 0;
    if ((dividend >= 0 && divisor > 0) || (dividend <= 0 && divisor < 0)) {
        sign = 1;
    }
    else {
        sign = -1;
    }
    dividend = Math.abs(dividend);
    divisor = Math.abs(divisor);
    while (dividend >= divisor) {
        dividend = dividend - divisor;
        quotient++;
    }
    return quotient * sign;
}
