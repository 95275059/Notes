# MATLABTips2--set和get

1. set

   + 设置图形对象属性

   + 语法

     + set(H,Name,Value)

       为H标识的对象指定其Name属性的值为Value

       使用时需要用单引号将属性名引起来    例：set(H,'Color','red')

       若H是对象的向量，则set会为所有对象设置属性

       若H为空（即[]）,set不执行任何操作，但不返回错误或警告

     ---

     + set(H,NameArray,ValueArray)

       使用单元格数组NameArray和ValueArray指定多个属性值

       要为m个图形对象中的每个图形对象设置n个属性值，将ValueArray指定为m*n的单元格数组

       + m = length(H)
       + n = NameArray中包含的属性名的数量

     ---

     + set(H,S)

       使用S指定多个属性值

       + S是一个结构体，其字段名称为对象属性名称，字段值是对应的属性值

     ---

     + s=set(H)

       返回H标识的对象的，可由用户设置的属性及其可能的值

       s是一个包含对象属性名和其对应字段值是的结构体

       如果不指定输出参数，会在屏幕上显示全部信息

       H必须为单个对象

     ---

     + values=set(H,Name)

       返回指定属性的可能值

       如果可能的值为字符向量，则set会在单元格数组values的元胞中返回每个值

       H必须为单个对象

     ---

   ---

---

2. get

   + 查询对象属性

   + 语法

     + v=get(h)

       返回h标识的图形对象的所有属性和属性值

       v是一个结构体，其字段名称为属性名，其值为对应的属性值

       h可以是单个对象或m*n对象数组

     + v=get(h,propertyName)

       返回特定属性propertyName的值

       使用时需要用单引号将属性名引起来

     + v=get(h,propertyArray)

       返回一个m*n单元格数组

       m=length(h)

       n为propertyArray中包含的属性名的个数

     + v=get(h,'default')

       以结构体数组返回对象h上当前定义的所有**默认值**

       字段名称为对象属性名称，字段值为对应的属性值

     + v=get(h,defaultTypeProperty)

       返回特定属性的当前默认值

       defaultTypeProperty是将单词default与对象类型（如Figure）和属性名称（如Color）串联在单引号内组合而成

       例：get(groot,'defaultFigureColor')

     + v=get(groot,'factory')

       以结构体数组返回所有用户可设置属性的**出场定义值**

       字段名称为对象属性名称，字段值为对应的属性值

     + v=get(groot,factoryTypeProperty)

       返回特定属性的出场默认值

       factoryTypeProperty将单词factory与对象类型（如Figure）和属性名称（如Color）串联在单引号内组合而成

       如：get(groot,'factoryFigureColor')

   + 例

     ```matlab
     get(0)
     ```

     + 输出

       ```matlab
       	CallbackObject = []
       	CommandWindowSize = [74 10]
       	CurrentFigure = []
       	Diary = off
       	DiaryFile = diary
       	Echo = off
       	FixedWidthFontName = Courier New
       	Format = short
       	FormatSpacing = loose
       	Language = en_us
       	MonitorPositions = [ (2 by 4) double array]
       	More = off
       	PointerLocation = [1258 102]
       	RecursionLimit = [500]
       	ScreenDepth = [32]
       	ScreenPixelsPerInch = [96]
       	ScreenSize = [1 1 1920 1080]
       	ShowHiddenHandles = off
       	Units = pixels
       
       	BeingDeleted = off
       	ButtonDownFcn = 
       	Children = []
       	Clipping = on
       	CreateFcn = 
       	DeleteFcn = 
       	BusyAction = queue
       	HandleVisibility = on
       	HitTest = on
       	Interruptible = on
       	Parent = []
       	Selected = off
       	SelectionHighlight = on
       	Tag = 
       	Type = root
       	UIContextMenu = []
       	UserData = []
       	Visible = on
       ```

       

   

   

   







