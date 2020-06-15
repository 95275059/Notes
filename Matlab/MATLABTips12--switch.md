# MATLABTips12--switch

+ 语法

  ```matlab
  switch 变量
  	case 常量1
  		语句序列1；
      case 常量2
          语句序列2；
      ........
      case 常量n
      	语句序列n;
      otherwise
          语句序列；
  end
  ```

+ 注

  otherwise是可选的

  找到匹配的case后，执行完自动退出，不必像C需要break

+ 例

  ```matlab
  switch type
  	case 'SBIRS'
  		add_object1=['Chains */Chain/',objects_name,' Add Satellite/',objects_name];
      otherwise
          add_object1=['Chains */Chain/',objects_name,' Add Facility/',objects_name];
  end
  ```

  