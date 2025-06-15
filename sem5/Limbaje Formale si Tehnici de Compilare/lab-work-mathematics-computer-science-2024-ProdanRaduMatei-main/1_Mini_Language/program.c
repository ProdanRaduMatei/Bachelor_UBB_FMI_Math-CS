start
int k;
int i;
int j;
int is_prime;

cin >> k;

i = 2;
while (i < k)
{
    is_prime = 1;
    j = 2;
    while (j * j <= i)
    {
        if (i % j == 0)
        {
            is_prime = 0;
            break;
        }
        j = j + 1;
    }
    if (is_prime == 1)
    {
        cout << i;
    }
    i = i + 1;
}
end