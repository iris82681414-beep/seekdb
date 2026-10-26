# seekdb 2026 基础实践材料

检查日期：2026-10-26。比赛成绩以参赛平台提测记录为准。

## 官方 Fork

- 地址：https://github.com/iris82681414-beep/seekdb
- GitHub 原生 Fork；API 已确认 `fork=true`、`parent.full_name=oceanbase/seekdb`、`private=false`。
- 默认分支：`master`。
- 本队验证行已原样独占一行写入默认分支 `README.md`，并通过远程文件读取核实。
- README 提交：`138a6eb0c63fd47fcc25f0a2273b49b06b00b7f0`。
- 可向比赛平台填写上述 Fork 地址；尚未获取平台判分结果。

## 官方 PR

尚未创建，不存在可提交的 PR 地址。

已阅读官方 `CONTRIBUTING.md`、开发指南、单元测试指南及 PR 模板。
当前比赛文档要求选取带 `2026-competition` 标签的 Issue，完成复现、分析、修复及测试。
从当前公开目录取得的 PR 子题地址为：
https://oceanbase.yuque.com/org-wiki-obtech-vh7w9r/hc3pio/xom0q8ni2ow8t9py

已经检查的大赛 Issue 中，常见的小型修复已有相关 PR，例如：

| Issue | 已有相关 PR | 方向 |
| --- | --- | --- |
| #1469 | #1665、#1676 等 | DDL 标识符转义的模块依赖 |
| #1477 | #1639、#1727 等 | 双重 NOT 简化后类型保持 |
| #1480 | #1570、#1627 等 | 无 MAC 环境的 UUID 初始化 |
| #1501 | #1615 | 等价 BETWEEN/OR 过滤性能 |
| #1512 | #1572、#1678 等 | 重复 IN 列表 |
| #1544 | #1673、#1718 等 | Windows 初始化超时 |
| #1549 | #1668 | 恢复事务的表锁 |

以上是选题检索结果，并不表示已独立验证这些 PR 的正确性或测试。
后续贡献需确认尚未覆盖的真实问题，避免提交重复修改。
实际 PR 开发分支必须直接从最新 `oceanbase/seekdb:master` 创建，不能包含 Fork 默认分支的比赛验证行提交。
本材料分支用于记录基础实践进度，不是向官方提交的代码贡献分支。

## AMD Radeon 部署

尚未创建或连接本队 AMD 实例，尚未取得部署 UUID、SQL 执行结果或遥测送达证据。
未以本地安装代替用户指定的 AMD 流程。

完整题目和 AMD 教程均已成功读取：

- 部署题：https://oceanbase.yuque.com/org-wiki-obtech-vh7w9r/hc3pio/lz6ixow11mar233g
- AMD 教程：https://oceanbase.yuque.com/org-wiki-obtech-vh7w9r/hc3pio/lcuknwgl955v8ou7

部署题当前注明 AMD 为可选资源；本任务仍按用户要求使用 AMD。
教程通过 `seekdb-hipvs` 模板提供预编译运行环境；具体版本以实际实例的自检结果为准。

需要用户先完成的账号网页步骤：

1. 登录 https://developer.amd.com.cn/login?source=0u9Eqno7R 。
2. 在“积分免费兑换”中兑换云算力券，进入“AMD 开发者云”。
3. 在 `Profile → Redeem Credits` 中兑换额度。
4. 在 `Gallery` 搜索 `seekdb-hipvs`，点击 `Launch`。
5. 看到 `Your workspace is ready` 后点击 `Open Notebook`。
6. 提供可用的终端或 SSH 连接方式；若仅支持 Notebook，执行模板自带的初始化、环境自检与启动单元。

教程截图的启动单元是 `sk.start_observer("/workspace/run/obs1")`，随后调用 `sk.version()`。
它依赖模板前面单元初始化的 `sk`，不能在未初始化的 Notebook 中直接执行。
截图出现的版本与目录只是教程示例，不是本队实测数据。

启动成功后，在同一 Notebook 内运行本目录 `amd-verification-cell.py` 的内容。
它只读取实际运行目录中的 `run/telemetry.json`，严格校验 `content.id`，不会生成 UUID。
默认运行目录来自教程截图；若实际启动目录不同，先修改 `runtime_dir`。
输出数据库版本和 GPU 自检信息，并区分本地送达标记与平台最终判定。

不要在尚未保存部署记录、UUID 和上报证据时销毁实例。

## 最终材料状态

| 任务 | 实际成果 | 验证状态 | 提测材料 |
| --- | --- | --- | --- |
| AMD 部署 | 尚未连接实例 | 待验证 | 尚无 UUID |
| 官方 Fork | 已创建公开原生 Fork，README 验证行已保存 | GitHub 已验证，比赛平台待验证 | https://github.com/iris82681414-beep/seekdb |
| 官方 PR | 尚未创建 | 待验证 | 尚无 PR URL |

两个私有报名仓库未执行写入、删除、重置、强制推送或可见性修改。
