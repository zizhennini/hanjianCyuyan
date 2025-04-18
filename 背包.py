num = []
N ,V = map(int,input().split())             # N 个物品的数量 和 V背包容量。
for i in range(2,N+1):
    w,v = map(int,input().split())          # 第 2∼N+1 行包含 2 个正整数 w,v，表示物品的体积和价值。
    num.append((w,v))
w_sum = [x[0] for x in num]
v_sum = [x[1] for x in num]
if V == w_sum:
    sum_w = sum(w_sum)
    #v_sum = sum(v_sum)

    print(sum_w)                                                                                                     ��器人初始位置在什么地方，
其清扫路径的本质都是重复两次 a 到 b，b 到 c，c 到 d 的过程，花费时间为 6，由此，假设某个机器人清扫的格子范围为 l,
那么这个机器人花费的时间为 (l-1)\times*2。所以只需要对机器人清扫的范围（l）进行二分即可，最后的答案为 t=(l-1)\times*2。

显然当每个机器人清扫的范围大小相同时，花费时间最小。
可以对清扫范围进行二分，然后验证其答案的正确性即可，判断条件是清扫范围可以使得每个格子都能够扫到

可以明显的知道，最左边的格子由左边第一台机器人清扫，花费时间是最少的，在此可以采用贪心的思想，
让每台机器人都要优先清扫其左边还未扫的到格子，然后再往右扫，在二分得到的范围下往右扫得越多越好，
这样可以减少右边下一个机器人需要往左扫的范围，增加其往右扫的范围，以此类推，可减少清扫时间。

综上，本题采用二分加贪心的思想解答。
"""





# 所有机器人打扫的格子差不多的时候，时间是最短，不知道怎么写代码
# N, K = map(int, input().split())    # N 个方格区域 K 台扫地机器人
# for i in range(1,N+1):
#     a = int(input())                # 扫地机器人所在的格子位置

num = []
Sum = 0
n,m=map(int,input().split())
for i in range(n):
    L,R=map(int,input().split())
    num.append(L)
num.sort()
for j in range(len(num)):
    Sum +=abs(num[j] - num[])
print(Sum)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;,
    &quot;settings.editor.selected.configurable&quot;: &quot;settings.sync&quot;
  }
}</component>
  <component name="RunManager">
    <configuration name="main" type="PythonConfigurationType" factoryName="Python" nameIsGenerated="true">
      <module name="Python解法" />
      <option name="ENV_FILES" value="" />
      <option name="INTERPRETER_OPTIONS" value="" />
      <option name="PARENT_ENVS" value="true" />
      <envs>
        <env name="PYTHONUNBUFFERED" value="1" />
      </envs>
      <option name="SDK_HOME" value="" />
      <option name="WORKING_DIRECTORY" value="$PROJECT_DIR$" />
      <option name="IS_MODULE_SDK" value="true" />
      <option name="ADD_CONTENT_ROOTS" value="true" />
      <option name="ADD_SOURCE_ROOTS" value="true" />
      <option name="SCRIPT_NAME" value="$PROJECT_DIR$/main.py" />
      <option name="PARAMETERS" value="" />
      <option name="SHOW_COMMAND_LINE" value="false" />
      <option name="EMULATE_TERMINAL" value="false" />
      <option name="MODULE_MODE" value="false" />
      <option name="REDIRECT_INPUT" value="false" />
      <option name="INPUT_FILE" value="" />
      <method v="2" />
    </configuration>
    <configuration name="物品名称末尾加s或es" type="PythonConfigurationType" factoryName="Python" temporary="true" nameIsGenerated="true">
      <module name="Python解法" />
      <option name="ENV_FILES" value="" />
      <option name="INTERPRETER_OPTIONS" value="" />
      <option name="PARENT_ENVS" value="true" />
      <envs>
        <env name="PYTHONUNBUFFERED" value="1" />
      </envs>
      <option name="SDK_HOME" value="" />
      <option name="WORKING_DIRECTORY" value="$PROJECT_DIR$" />
      <option name="IS_MODULE_SDK" value="true" />
      <option name="ADD_CONTENT_ROOTS" value="true" />
      <option name="ADD_SOURCE_ROOTS" value="true" />
      <option name="SCRIPT_NAME" value="$PROJECT_DIR$/物品名称末尾加s或es.py" />
      <option name="PARAMETERS" value="" />
      <option name="SHOW_COMMAND_LINE" value="false" />
      <option name="EMULATE_TERMINAL" value="false" />
      <option name="MODULE_MODE" value="false" />
      <option name="REDIRECT_INPUT" value="false" />
      <option name="INPUT_FILE" value="" />
      <method v="2" />
    </configuration>
    <recent_temporary>
      <list>
        <item itemvalue="Python.物品名称末尾加s或es" />
      </list>
    </recent_temporary>
  </component>
  <component name="SharedIndexes">
    <attachedChunks>
      <set>
        <option value="bundled-python-sdk-495700d161d3-aa17d162503b-com.jetbrains.pycharm.community.sharedIndexes.bundled-PC-243.22562.220" />
      </set>
    </attachedChunks>
  </component>
  <component name="SpellCheckerSettings" RuntimeDictionaries="0" Folders="0" CustomDictionaries="0" DefaultDictionary="应用程序级" UseSingleDictionary="true" transferred="true" />
  <component name="TaskManager">
    <task active="true" id="Default" summary="默认任务">
      <changelist id="b921a17e-77be-427b-b00b-f86ee385e550" name="更改" comment="" />
      <created>1739458580936</created>
      <option name="number" value="Default" />
      <option name="presentableId" value="Default" />
      <updated>1739458580936</updated>
    </task>
    <servers />
  </component>
  <component name="XDebuggerManager">
    <breakpoint-manager>
      <breakpoints>
        <line-breakpoint enabled="true" suspend="THREAD" type="python-line">
          <url>file://$PROJECT_DIR$/main.py</url>
          <line>8</line>
          <option name="timeStamp" value="1" />
        </line-breakpoint>
      </breakpoints>
    </breakpoint-manager>
  </component>
</project>                                                                                                                                                                                                              