import argparse
import sys
from src.scanner import find_markdown_files

def main():
    # 设置命令行参数
    parser = argparse.ArgumentParser(description="Markdown 文档检查与清洗工具")
    parser.add_argument("-d", "--dir", type=str, required=True, help="指定要扫描的目录路径")
    args = parser.parse_args()

    target_dir = args.dir
    print(f"开始扫描目录: {target_dir}")
    
    # 调用扫描模块
    md_files = find_markdown_files(target_dir)
    print(f"共发现 {len(md_files)} 个 Markdown 文件:")
    for f in md_files:
        print(f" - {f}")

if __name__ == "__main__":
    main()
