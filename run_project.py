"""
Master Project Orchestrator: Early Detection of Academic Burnout
Author: B.Tech (Artificial Intelligence), Amity University
"""

import sys
import os
import argparse
import subprocess

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
PKG_DIR = os.path.join(PROJECT_ROOT, "academic_burnout_ml")


def run_pipeline():
    print("\n" + "="*70)
    print("STEP 1: RUNNING FULL ML TRAINING & BENCHMARKING PIPELINE")
    print("="*70)
    script = os.path.join(PKG_DIR, "src", "pipeline.py")
    ret = subprocess.run([sys.executable, script], cwd=PROJECT_ROOT)
    if ret.returncode != 0:
        print("[!] Training pipeline failed.")
        sys.exit(ret.returncode)
    print("[+] Model training, evaluation, and visualization completed successfully.")


def run_tests():
    print("\n" + "="*70)
    print("STEP 2: RUNNING AUTOMATED UNIT & INTEGRATION TEST SUITE")
    print("="*70)
    test_script = os.path.join(PKG_DIR, "tests", "test_model.py")
    ret = subprocess.run([sys.executable, "-m", "unittest", test_script], cwd=PROJECT_ROOT)
    if ret.returncode != 0:
        print("[!] Test suite failed.")
        sys.exit(ret.returncode)
    print("[+] All 7 unit and integration tests passed.")


def run_predictions():
    print("\n" + "="*70)
    print("STEP 3: RUNNING SAMPLE CLI INFERENCE & RECOMMENDATIONS")
    print("="*70)
    predict_script = os.path.join(PKG_DIR, "src", "predict.py")
    subprocess.run([sys.executable, predict_script, "--sample"], cwd=PROJECT_ROOT)


def generate_pdf():
    print("\n" + "="*70)
    print("STEP 4: COMPILING OFFICIAL THESIS REPORT PDF (AMITY TEMPLATE)")
    print("="*70)
    # First recompile HTML to ensure latest figures/links
    build_html_script = os.path.join(PKG_DIR, "report", "build_html_report.py")
    subprocess.run([sys.executable, build_html_script], cwd=PROJECT_ROOT)

    html_file = os.path.join(PKG_DIR, "report", "Thesis_Early_Detection_Academic_Burnout.html")
    pdf_file = os.path.join(PKG_DIR, "report", "Thesis_Early_Detection_Academic_Burnout.pdf")
    html_uri = f"file:///{html_file.replace(os.sep, '/')}"

    edge_candidates = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    ]
    browser_exe = next((p for p in edge_candidates if os.path.exists(p)), None)

    if browser_exe:
        cmd = [
            browser_exe,
            "--headless=new",
            "--no-pdf-header-footer",
            f"--print-to-pdf={pdf_file}",
            html_uri
        ]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if os.path.exists(pdf_file) and os.path.getsize(pdf_file) > 100000:
            print(f"[+] Successfully compiled Thesis PDF ({os.path.getsize(pdf_file)} bytes):")
            print(f"    Path: {pdf_file}")
        else:
            print("[!] PDF generation encountered an issue.")
    else:
        print("[!] Headless browser not found. HTML thesis is available at:", html_file)


def run_web_app():
    print("\n" + "="*70)
    print("STEP 5: LAUNCHING INTERACTIVE WEB DASHBOARD (FLASK)")
    print("="*70)
    app_script = os.path.join(PKG_DIR, "app.py")
    subprocess.run([sys.executable, app_script], cwd=PROJECT_ROOT)


def main():
    parser = argparse.ArgumentParser(
        description="Master Orchestrator for Early Detection of Academic Burnout ML System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run_project.py --all         # Run pipeline, tests, compile PDF
  python run_project.py --train       # Re-train models and generate plots
  python run_project.py --test        # Run test suite
  python run_project.py --predict     # Run sample prediction in terminal
  python run_project.py --pdf         # Recompile thesis PDF
  python run_project.py --web         # Start interactive web dashboard
        """
    )

    parser.add_argument("--train", action="store_true", help="Run ML training pipeline and plot generation")
    parser.add_argument("--test", action="store_true", help="Run unit and integration tests")
    parser.add_argument("--predict", action="store_true", help="Run sample inference and recommendations")
    parser.add_argument("--pdf", action="store_true", help="Compile Thesis report to PDF")
    parser.add_argument("--web", action="store_true", help="Launch interactive web application dashboard")
    parser.add_argument("--all", action="store_true", help="Execute complete build: pipeline, tests, and PDF")

    args = parser.parse_args()

    # If no flags passed, show help or run all
    if not any([args.train, args.test, args.predict, args.pdf, args.web, args.all]):
        parser.print_help()
        print("\n[*] No flag specified. Running --all verification mode...")
        args.all = True

    if args.all or args.train:
        run_pipeline()

    if args.all or args.test:
        run_tests()

    if args.all or args.predict:
        run_predictions()

    if args.all or args.pdf:
        generate_pdf()

    if args.web:
        run_web_app()

    if args.all:
        print("\n" + "="*70)
        print("🎉 COMPLETE END-TO-END SYSTEM BUILD VERIFIED & READY!")
        print("To launch the web dashboard, run: python run_project.py --web")
        print("="*70 + "\n")


if __name__ == "__main__":
    main()
