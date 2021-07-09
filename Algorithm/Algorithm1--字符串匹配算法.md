# Algorithm1--字符串匹配算法

## 介绍

* 字符串匹配算法，通常输入为原字符串（string）和子串（pattern），要求返回子串在原字符串中首次出现的位置。

  比如原字符串为“ABCDEFG”，子串为“DEF”，则算法返回3。

* 常见的算法包括：BF（Brute Force，暴力检索）、RK（Robin-Karp，哈希检索）、KMP（教科书上最常见算法）、BM（Boyer Moore）、Sunday等

## 例题

> 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
> 测试用例：
> haystack = "hello", needle = "ll" : 2;
> haystack = "aaaaa", needle = "bba" : -1;

## BF(Brute Force，暴力检索)

### 思路

* 我们可以让字符串 needle 与字符串 haystack 的所有长度为 m 的子串均匹配一次
* 为了减少不必要的匹配，我们每次匹配失败即立刻停止当前子串的匹配，对下一个子串继续匹配。
* 如果当前子串匹配成功，我们返回当前子串的开始位置即可。如果所有子串都匹配失败，则返回 −1。

### 代码

```java
public class ImplementStrstr28 {
	public int strStr(String haystack, String needle) {
		// BF暴力检索
		// 时间击败43.04%，内存击败64.45%
		int nlen = needle.length(), hlen = haystack.length();
		if (nlen==0)
			return 0;
		else if (hlen==0)
			return -1;
		for (int i=0; i<=hlen-nlen; ++i) {
			boolean flag = true;
			for (int j=0; j<nlen; ++j) {
				if (haystack.charAt(i+j)!=needle.charAt(j)) {
					flag = false;
					break;
				}
			}
			if (flag)
				return i;
		}
		return -1;
    }	
}
```

## KMP(Knuth-Morris-Pratt 算法)

### 介绍

* Knuth-Morris-Pratt 算法，简称 KMP 算法，由Donald Knuth、James H. Morris 和 Vaughan Pratt 三人于 1977 年联合发表。

* Knuth-Morris-Pratt 算法的核心为前缀函数，π(i)，其定义如下：

  对于长度为 m 的字符串 s，其前缀函数 π(i)(0≤i<m) 表示 s 的子串 s[0:i] 的最长的相等的真前缀与真后缀的长度。

  特别地，如果不存在符合条件的前后缀，那么 π(i)=0。

  其中真前缀与真后缀的定义为不等于自身的前缀与后缀。

* 示例

  字符串 aabaaab 的前缀函数值依次为 0,1,0,1,2,2,30,1,0,1,2,2,3

  * π(0)=0，因为 a 没有真前缀和真后缀，根据规定为 0（可以发现对于任意字符串π(0)=0 必定成立）；
  * π(1)=1，因为 aa 最长的一对相等的真前后缀为 a，长度为 1；
  * π(2)=0，因为 aab 没有对应真前缀和真后缀，根据规定为 0；
  * π(3)=1，因为 aaba 最长的一对相等的真前后缀为 a，长度为 1；
  * π(4)=2，因为 aabaa 最长的一对相等的真前后缀为 aa，长度为 2；
  * π(5)=2，因为 aabaaa 最长的一对相等的真前后缀为 aa，长度为 2；
  * π(6)=3，因为 aabaaab 最长的一对相等的真前后缀为 aab，长度为 3。

* 有了前缀函数，我们就可以快速地计算出模式串在主串中的每一次出现。

### 如何求解前缀函数

https://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html

* 部分匹配表

### 代码

```java
public class ImplementStrstr28 {
	public int strStr1(String haystack, String needle) {
		// KMP
		// 时间击败18.74%，内存击败41.60%
		int nlen = needle.length(), hlen = haystack.length();
		if (nlen==0)
			return 0;
		else if (hlen==0)
			return -1;
		int[] npi = new int[nlen];
		for (int i=1, j=0; i<nlen; ++i) {
			while (j>0 && needle.charAt(i)!=needle.charAt(j)) 
				j = npi[j-1];
			if (needle.charAt(i) == needle.charAt(j))
				j++;
			npi[i]=j;
		}
		int i=0,j=0;
		while (i<=hlen-nlen && j<nlen) {
			while(j<nlen && haystack.charAt(i+j) == needle.charAt(j)) {
				++j;
			}
			if (j==0) {
				i+=1;
				continue;
			} 
			else if (j==nlen)
				return i;
			else {
				i += j-npi[j-1];
				j = npi[j-1];
			}
		}
		return -1;
	}
}
```











