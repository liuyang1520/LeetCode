/*
x(x+1)/2 = n
x**2 + x - 2n = 0
x = (-1 + (1+8n)**0.5)/2
*/
func arrangeCoins(n int) int {
    return (int(math.Pow(float64(1+8*n), 1.0/2)) - 1) / 2
}
