# hardware-interface-contract

这是一个 Codex Skill，用于从芯片手册、原理图、接口表、调试日志和既有固件中提取可审查、可落地的硬件接口契约。

核心输出是 `hardware-interface-contract.json`，帮助固件工程师明确引脚、总线、上电/复位、寄存器初始化、风险和待验证问题。

技能目录：

- `hardware-interface-contract/SKILL.md`
- `hardware-interface-contract/references/contract-format.md`
- `hardware-interface-contract/scripts/validate_contract.py`

验证：

```powershell
python C:\Users\ASUS\.codex\skills\.system\skill-creator\scripts\quick_validate.py .\hardware-interface-contract
```
