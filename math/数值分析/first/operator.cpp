 #include <iostream>
 #include <string>
 using namespace std;
 
 string clearZeros(string data)
 {
     if (data[0] == '0') {
        int key = (int) data.length() - 1;
        for (int i = 0; i < data.length(); i++) {
            if (data[i] != '0') {
                key = i;
                break;
           }
       }
       data.erase(0, key);
}
     if (data == "") {
        data = "0";
    }
    return data;
}
 
 //对位操作
 void countPoint(string &operand1, string &operand2)
 {
    while (operand1.length() < operand2.length()) {
        operand1 = "0" + operand1;
    }
    while (operand1.length() > operand2.length()) {
        operand2 = "0" + operand2;
    }
}

//判断大小
bool bigger(string operand1, string operand2)
{
    return operand1 >= operand2;
}

string addition(string addent, string adder)
{
//先对位，在加数和被加数前面适当补0，使他们包含相同的位数
countPoint(addent, adder);
//前面再补一个0，确定和的最多位数
addent = "0" + addent;
adder = "0" + adder;
//从低位开始，对应位相加，结果写进被加数中，如果有进位，直接给被加数前一位加1
for (int i = (int) addent.length() - 1; i > 0; i--) {
    addent[i] = addent[i] + adder[i] - 48;
    if (addent[i] > '9') {
    addent[i] = addent[i] - 10;
	addent[i - 1] = addent[i - 1] + 1;
		}
    }
    return clearZeros(addent);
}

string subtraction(string subtrahend, string subtractor)
{
//先对位，在减数和被减数前面适当补0，使他们包含相同的位数
countPoint(subtrahend, subtractor);
//判断被减数和减数谁大，保证被减数大于减数
   if (bigger(subtrahend, subtractor)) {
	   subtrahend[0] = subtrahend[0] - subtractor[0] + 48;
        for (int i = 1; i < (int)subtrahend.length(); i++) {
		    if (subtrahend[i] >= subtractor[i]) {
		    subtrahend[i] = subtrahend[i] - subtractor[i] + 48;
            } 
		else {
        subtrahend[i] = subtrahend[i] - subtractor[i] + 10 + 48;
        subtrahend[i - 1]--;
		      }
        }
    } 
    else {
       subtrahend = '-' + subtraction(subtractor, subtrahend);
    }
    return subtrahend;
}

string multiplication(string multiplicand, string multiplier)
{
    string result = "0";
    for (int i = (int)multiplier.length() - 1; i >= 0 ; i--) {
        for (char c = '1'; c <= multiplier[i]; c++) {
            result = addition(result, multiplicand);
        }
    multiplicand = multiplicand + "0";
    }
    return clearZeros(result);
}

// 试商法
string division(string dividend, string divisor)
{
// 存放商
string result;
// 存放余数
string remains;
for (int i = 0; i < (int)dividend.length(); i++) {
    remains = remains + dividend[i];
    result = result + "0";
    // 从1往上试
    while (bigger(remains, result)) {
    cout << result << "-----------" << remains << endl;
    result[result.length() - 1]++;
    remains = subtraction(remains, divisor);
        }
    }
    return clearZeros(result);
}
int main(int argc, const char * argv[])
{
string a, b;
int tests;
cin >> tests;
//while (tests--) {
    cin >> a >> b;
    //正整数高精度加法，从低位开始
    cout << addition(a, b) << endl;
    //正整数高精度减法，从高位开始
    //cout << subtraction(a, b) << endl;
    //正整数高精度乘法，将乘法转换为加法进行运算
    //cout << multiplication(a, b) << endl;
    //cout << division(a, b) << endl;
    //正整数高精度除法
   // }
   return 0;
}