import argparse
import sys
from src.scanner import find_markdown_files
from src.checker import check_links
from src.parser import parse_headings

def main():
    parser = argparse.ArgumentParser(description="Markdown 文档检查与清洗工具")
    parser.add_argument("-d", "--dir", type=str, required=True, help="指定要扫描的目录路径")
    args = parser.parse_args()

    target_dir = args.dir
    print(f"开始扫描目录: {target_dir}\n")
    
    md_files = find_markdown_files(target_dir)
    print(f"共发现 {len(md_files)} 个 Markdown 文件:\n")
    
    total_errors = 0
    for f in md_files:
        print(f"========== 正在处理: {f} ==========")
        
        # 1. 检测死链
        errors = check_links(f)
        if errors:
            for err in errors:
                print(f"  [❌] {err}")
                total_errors += 1
        else:
            print("  [✅] 未发现死链接或损坏图片")
            
        # 2. 统计标题
        stats, headings = parse_headings(f)
        print("  [📊] 标题层级统计:")
        for level, count in stats.items():
            if count > 0:
                print(f"       H{level}: {count} 个")
                
        # 3. 生成目录索引 (展示前几个)
        if headings:
            print("  [📑] 目录索引预览:")
            for level, title in headings[:3]: # 只打印前3个标题做个演示
                indent = "  " * (level - 1)
                print(f"       {indent}- {title}")
            if len(headings) > 3:
                print("       ... (省略后续)")
        print() # 空一行方便阅读
            
    print(f"全部检查完成，共发现 {total_errors} 处链接/图片错误。")

if __name__ == "__main__":
    main()
