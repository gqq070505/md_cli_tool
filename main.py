import argparse
import sys
from src.scanner import find_markdown_files
from src.checker import check_links

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
        print(f"正在检查: {f}")
        errors = check_links(f)
        if errors:
            for err in errors:
                print(f"  [❌] {err}")
                total_errors += 1
        else:
            print("  [✅] 未发现死链接或损坏图片")
            
    print(f"\n检查完成，共发现 {total_errors} 处问题。")

if __name__ == "__main__":
    main()
