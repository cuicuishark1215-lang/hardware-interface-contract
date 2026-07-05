# hardware-interface-contract

一个面向固件、硬件评审和板级调试的 Codex Skill：把芯片手册、原理图、接口表、调试日志和既有固件交叉校验，整理成可审查、可执行的硬件接口契约。

## 它解决什么问题

硬件项目里最容易丢信息的地方，往往不是手册本身，而是手册、原理图和固件之间的缝隙：

- 手册写了时序、电压、启动脚和寄存器要求，但固件初始化没有跟上。
- 原理图里的网络名、片选、中断脚和代码里的宏定义对不上。
- 旧项目能跑，但没人知道哪些配置是板级约束，哪些只是历史偶然。
- 新板 bring-up 时，问题散落在聊天记录、口头描述、日志和数据手册里。

这个 Skill 的目标是把这些分散证据变成一份 `hardware-interface-contract.json`，让固件工程师能直接写驱动、改设备树、做初始化和设计调试步骤。

## 适用场景

- 从芯片手册提取关键接口、引脚、电源、复位、启动和寄存器约束。
- 从原理图说明或引脚表整理 MCU 到外设的总线连接。
- 对照旧固件，找出驱动假设、宏定义、片选、中断、电源控制和初始化寄存器。
- 为新板 bring-up 生成可执行检查清单。
- 为硬件评审输出风险、冲突和待验证问题。
- 为量产测试整理接口、测点和工厂检查项。

## 输出内容

主要输出：

```text
hardware-interface-contract.json
```

契约会尽量覆盖：

- 器件、连接器、网络名和电压域。
- 总线类型、地址、片选、速率、模式和上下拉。
- MCU 引脚、复用功能、方向、复位状态和电气限制。
- 上电顺序、复位脚、启动配置、时钟和延迟要求。
- 初始化关键寄存器、掩码、取值、原因和证据来源。
- 固件任务、风险、开放问题和实验室验证建议。

## 安装方式

克隆仓库：

```powershell
git clone https://github.com/cuicuishark1215-lang/hardware-interface-contract.git
```

复制 Skill 目录到本机 Codex skills 目录：

```powershell
Copy-Item -Recurse .\hardware-interface-contract "$env:USERPROFILE\.codex\skills\"
```

然后在 Codex 中使用：

```text
使用 $hardware-interface-contract 从手册、原理图说明和既有固件中提取固件可用的硬件接口契约。
```

## 仓库结构

```text
hardware-interface-contract/
  SKILL.md
  agents/openai.yaml
  references/contract-format.md
  scripts/validate_contract.py
```

## 校验

校验 Skill 格式：

```powershell
python C:\Users\ASUS\.codex\skills\.system\skill-creator\scripts\quick_validate.py .\hardware-interface-contract
```

校验生成的接口契约：

```powershell
python .\hardware-interface-contract\scripts\validate_contract.py .\hardware-interface-contract.json
```

## 搜索关键词

这些关键词用于帮助别人通过 GitHub 搜到这个仓库：

```text
codex-skill
ai-skill
hardware-interface
firmware
embedded
datasheet
schematic
pcb
bringup
board-bringup
driver
registers
i2c
spi
uart
硬件接口契约
芯片手册提取
原理图接口分析
固件开发
板级调试
```

## 适合谁

- 正在做新板 bring-up 的固件工程师。
- 需要把原理图转成驱动任务的嵌入式团队。
- 想把口头硬件经验沉淀成可审查文档的硬件负责人。
- 需要快速理解旧项目硬件接口和固件假设的维护者。
