## PARS

---

### 一句话概括

CM理论基础，蒸馏是重点

---

### Problem

解决传统diffusion的生成速度问题，在保持高质量时追求一步到位（确定性

---

### Approach

diffusion使用Karras (EDM) 体系，在这个设置下概率流ODE变得十分简洁：$\frac{dx}{dt} = -t s_\phi(x, t)$，使得轨迹更加平直

CM要满足在时间t是一个很小的值时，模型输出等于输入本身，而EDM含有一个类似的Skip Connection写法：$D_\theta(x; \sigma) = c_{skip}(\sigma)x + c_{out}(\sigma)F_\theta(x; \sigma)$，经过微调，设置 $c_{skip}(\epsilon)=1$ 和 $c_{out}(\epsilon)=0$，强制模型在 $t=\epsilon$ 时变为恒等映射

所以说轨迹直的ODE，会很适合CD，也就是一致性蒸馏，可以把推理步数变成1步

一致性定义：在一条ODE轨迹上的输入，输出必须相同。边界条件即为上文提到的恒等

具体蒸馏方式就是给定数据，加噪，到t+1时间步时再走一步得到t时间步，两个数据和时间步丢给CM，要求输出一致（有专门loss

---

### Result

支持少步高质量生成，并且有零样本编辑能力（说明真正学到了流形）

编辑任务可以在加去噪中加入替换步

---

### Summary

理论基础，打通蒸馏这一块的思路
