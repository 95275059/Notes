# Python模块23--sched

## 简介

* sched是一个通用时间调度器，在调度器里使用一个延迟函数等待特定的时间，然后执行任务
* sched同时支持多线程应用程序， 在每个任务执行后会立刻调用延时函数，以确保其他线程也能执行
* python 标准库

## 使用

* class sched.scheduler(timefunc, delayfunc)这个类定义了调度事件的通用接口，它需要外部传入两个参数
  + time_func是一个没有参数的返回时间类型数字的函数，常使用的如time模块里的time
  + delayfunc应该是一个需要一个参数来调用，与timefunc的输出兼容，并且作为延迟多个时间单位的函数，常使用的如time模块的sleep
  + 