import os
import re

# 匹配规则：数字开头 + 点 + 主题 + .md
# Group 1: 序号, Group 2: 主题内容
PATTERN = re.compile(r'^(\d+)\.(.+)\.md$')

def main():
    # 1. 自动定位脚本所在目录（不硬编码，复制到哪个文件夹就在哪生效）
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"📂 当前工作目录: {current_dir}")

    # 2. 获取用户输入
    try:
        input_str = input("👉 请输入要插入（空出）的起始序号 (例如想在 08 处插入，就输 08): ")
        target_index = int(input_str)
    except ValueError:
        print("❌ 错误：请输入纯数字。")
        return

    # 3. 扫描文件并筛选
    files_to_move = []
    
    for filename in os.listdir(current_dir):
        # 跳过脚本文件自己
        if filename == os.path.basename(__file__):
            continue
            
        match = PATTERN.match(filename)
        if match:
            idx = int(match.group(1))
            topic = match.group(2)
            
            # 只有序号 >= 目标序号的文件才需要移动
            if idx >= target_index:
                files_to_move.append({
                    'old_name': filename,
                    'idx': idx,
                    'topic': topic
                })

    if not files_to_move:
        print(f"⚠️ 未找到序号大于等于 {target_index} 的 .md 文件。")
        return

    # 4. 关键算法：按序号【从大到小】排序
    # 必须倒序操作（例如先动 17->18，再动 16->17），防止覆盖中间的文件
    files_to_move.sort(key=lambda x: x['idx'], reverse=True)

    print(f"\n🔍 共找到 {len(files_to_move)} 个文件需要后移。")
    print(f"   预览: {files_to_move[-1]['old_name']} (最小) -> 将变为 {target_index+1:02d}...")
    
    # 二次确认（防止手滑）
    if input("🚀 确认执行吗? (y/n): ").strip().lower() != 'y':
        print("已取消。")
        return

    # 5. 执行重命名
    count = 0
    for item in files_to_move:
        # 新序号 = 旧序号 + 1
        new_idx = item['idx'] + 1
        # 格式化：保持两位数补零 (08, 09, 10...)
        new_name = f"{new_idx:02d}.{item['topic']}.md"
        
        old_path = os.path.join(current_dir, item['old_name'])
        new_path = os.path.join(current_dir, new_name)
        
        os.rename(old_path, new_path)
        print(f"   ✅ {item['old_name']} -> {new_name}")
        count += 1

    print(f"\n✨ 完成！已将 {count} 个文件序号后移。")
    print(f"📝 现在你可以新建文件：{target_index:02d}.xxx.md 了")

if __name__ == "__main__":
    main()