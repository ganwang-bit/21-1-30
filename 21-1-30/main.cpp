//#include <iostream>
//
//using namespace std;
//
//int main()
//{
//    cout << "Hello world!" << endl;
//    return 0;
//}
//#include<stdio.h>
//int main()
//{
//    printf("Programming in C is fun!");
//    return 0;
//}
//#include<iostream>
//using namespace std;
//int main()
//{
//    cout<<"Programming in C is fun!"<<endl;
//    return 0;
//}
//#include<stdio.h>
//int count=0;
//int main()
//{
//    int n;
//    scanf("%d",&n);
//    while(n!=1)
//    {
//        if(n%2)
//            n=(3*n+1)/2;
//        else
//            n=n/2;
//        count++;
//    }
//    printf("%d",count);
//    return 0;
//}
//#include<iostream>
//using namespace std;
//int main()
//{
//    int count=0,n;
//    cin>>n;
//    while(n!=1)
//    {
//        if(n%2)
//            n=(3*n+1)/2;
//        else
//            n/=2;
//        count++;
//    }
//    cout<<count;
//    return 0;
//}
//#include<stdio.h>
//const char *arr[10]={"ling","yi","er","san","si","wu","liu","qi","ba","jiu"};
//void f(int sum)
//{
//    if(!(sum/10))
//    {
//        printf("%s",arr[sum%10]);
//        return ;
//    }
//    else
//        f(sum/10);
//    printf(" %s",arr[sum%10]);
//}
//int main()
//{
//    char tmp;
//    int sum=0;
//    while(scanf("%c",&tmp)&&tmp!='\n')
//    {
//        sum+=tmp-'0';
//    }
//    f(sum);
//    return 0;
//}
//#include<iostream>
//using namespace std;
//const char *arr[10]={"ling","yi","er","san","si","wu","liu","qi","ba","jiu"};
//void f(int sum)
//{
//    if(!(sum/10))
//    {
//        cout<<arr[sum%10];
//        return ;
//    }
//    else
//        f(sum/10);
//    cout<<" "<<arr[sum%10];
//}
//int main()
//{
//    char tmp;
//    int sum=0;
//    while(cin>>tmp&&tmp!='\n')
//    {
//        sum+=tmp-'0';
//    }
//    f(sum);
//    return 0;
//}
//
