# 硬件接口契约格式

使用 JSON 作为机器可读契约。字段要小、明确、可追溯。

## 最小结构

```json
{
  "contract_version": "1.0",
  "project": "board-or-product-name",
  "generated_from": [
    {
      "source": "datasheet.pdf",
      "kind": "datasheet",
      "notes": "pages 12-45 reviewed"
    }
  ],
  "components": [],
  "interfaces": [],
  "pins": [],
  "power": [],
  "boot_reset": [],
  "registers": [],
  "firmware_tasks": [],
  "risks": [],
  "open_questions": []
}
```

## 置信度

只使用这些值：

- `high`：至少被一个权威来源确认，且没有冲突证据。
- `medium`：从上下文合理推断，或被一个非权威来源确认。
- `low`：合理但未验证、存在冲突，或依赖缺失资料。

所有会影响固件行为的对象都应包含 `confidence` 和 `evidence`。

## 接口对象

```json
{
  "name": "imu_spi",
  "type": "spi",
  "controller": "mcu",
  "peripheral": "u3",
  "signals": [
    {"name": "SCK", "net": "IMU_SCK", "pin": "PA5"}
  ],
  "settings": {
    "mode": "0",
    "max_hz": 10000000
  },
  "confidence": "medium",
  "evidence": ["schematic sheet 3", "datasheet p.18"]
}
```

## 引脚对象

```json
{
  "component": "mcu",
  "pin": "PB6",
  "net": "I2C1_SCL",
  "function": "i2c_scl",
  "direction": "open-drain",
  "voltage_domain": "3v3",
  "reset_state": "input",
  "confidence": "high",
  "evidence": ["schematic sheet 2"]
}
```

## 风险对象

```json
{
  "severity": "high",
  "summary": "I2C pull-up voltage differs from sensor absolute maximum",
  "impact": "May damage sensor or prevent bus communication",
  "evidence": ["schematic sheet 4", "datasheet p.7"],
  "recommended_check": "Measure pull-up rail on R21/R22 before powering sensor"
}
```

## 写作规则

- 优先使用小对象数组，少用长段落字段。
- 寄存器只记录初始化、安全性或板级差异必需的值。
- 不知道就写 `unknown`，不要猜值。
- 未解决矛盾如果会影响硬件安全或 bring-up，要同时写入相关对象和 `risks`。
