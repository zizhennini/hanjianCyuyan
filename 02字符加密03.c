#include <stdio.h>
//定义main函数
int main()
{
    char c1, c2, c3, c4, c5;
    //请在此添加‘字符加密’的代码
    /*****************Begin******************/
    scanf_s("%c%c%c%c%c", &c1, &c2, &c3, &c4, &c5);
    if ('A' <= c1 && c1 <= 'Z')
        c1 = (c1 - 'A' + 4) % 26 + 'A';
    else if ('a' <= c1 && c1 <= 'z')
        c1 = (c1 - 'a' + 4) % 26 + 'a';
    if ('A' <= c2 && c2 <= 'Z')
        c2 = (c2 - 'A' + 4) % 26 + 'A';
    else if ('a' <= c2 && c2 <= 'z')
        c2 = (c2 - 'a' + 4) % 26 + 'a';
    if ('A' <= c3 && c3 <= 'Z')
        c3 = (c3 - 'A' + 4) % 26 + 'A';
    else if ('a' <= c3 && c3 <= 'z')
        c3 = (c3 - 'a' + 4) % 26 + 'a';
    if ('A' <= c4 && c4 <= 'Z')
        c4 = (c4 - 'A' + 4) % 26 + 'A';
    else if ('a' <= c4 && c4 <= 'z')
        c4 = (c4 - 'a' + 4) % 26 + 'a';
    if ('A' <= c5 && c5 <= 'Z')
        c5 = (c5 - 'A' + 4) % 26 + 'A';
    else if ('a' <= c5 && c5 <= 'z')
        c5 = (c5 - 'a' + 4) % 26 + 'a';
    printf("%c%c%c%c%c", c1, c2, c3, c4, c5);
    /***************** End ******************/
    return 0;
}
