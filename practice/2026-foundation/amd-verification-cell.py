"""在 AMD 模板原有 Notebook 完成初始化和启动后，粘贴为一个新代码单元运行。"""

import json
from pathlib import Path
from uuid import UUID

# 与实际 sk.start_observer(...) 的目录保持一致。
runtime_dir = Path("/workspace/run/obs1")
telemetry_path = runtime_dir / "run" / "telemetry.json"

if "sk" not in globals():
    raise RuntimeError("请先执行 AMD 模板 Notebook 的初始化、自检及 seekdb 启动单元。")
if not telemetry_path.is_file():
    raise FileNotFoundError(
        f"未找到 {telemetry_path}；请核对实际运行目录及 seekdb 启动结果，不要生成替代 UUID。"
    )

telemetry = json.loads(telemetry_path.read_text(encoding="utf-8"))
deployment_uuid = telemetry["content"]["id"]
if (
    not isinstance(deployment_uuid, str)
    or len(deployment_uuid) != 36
    or str(UUID(deployment_uuid)) != deployment_uuid.lower()
):
    raise ValueError("content.id 不是包含连字符的完整标准 UUID。")

evidence = {
    "source": str(telemetry_path.resolve()),
    "deployment_uuid": deployment_uuid,
    "seekdb_version": sk.version(),
    "gpu_info": sk.gpu_info(),
    "local_sent_flag": telemetry.get("sent", "文件中未提供 sent 字段"),
    "platform_verification": "尚未查询比赛平台，文件存在本身不能证明遥测已送达",
}
print(json.dumps(evidence, ensure_ascii=False, indent=2, default=str))
