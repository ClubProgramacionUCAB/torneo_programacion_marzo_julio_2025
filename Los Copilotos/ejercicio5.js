function ejercicio5(dividend, divisor) {
    let quotient = 0;
    let sign = dividend * divisor < 0 ? -1 : 1;
    dividend = Math.abs(dividend);
    divisor = Math.abs(divisor);
    while (dividend > divisor) {
        dividend = dividend - divisor;
        quotient++;
    }

    return quotient * sign;
}
