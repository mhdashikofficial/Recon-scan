import subprocess
import argparse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def run_nmap(domain):
    result = subprocess.run(['nmap', '-sV', domain], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def run_dirbuster(domain):
    result = subprocess.run(['dirbuster', '-u', domain], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def run_sublist3r(domain):
    result = subprocess.run(['sublist3r', '-d', domain], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def run_recon_ng(domain):
    result = subprocess.run(['recon-ng', 'recon/domains-hosts/hackertarget', 'set SOURCE '+domain, 'run'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def main(domain):
    nmap_output = run_nmap(domain)
    dirbuster_output = run_dirbuster(domain)
    sublist3r_output = run_sublist3r(domain)
    recon_ng_output = run_recon_ng(domain)

    # Save output to PDF file
    pdf_file = domain + '_output.pdf'
    c = canvas.Canvas(pdf_file, pagesize=letter)
    c.drawString(100, 700, 'Nmap Output:')
    c.drawString(100, 675, nmap_output)
    c.drawString(100, 575, 'Dirbuster Output:')
    c.drawString(100, 550, dirbuster_output)
    c.drawString(100, 450, 'Sublist3r Output:')
    c.drawString(100, 425, sublist3r_output)
    c.drawString(100, 325, 'Recon-ng Output:')
    c.drawString(100, 300, recon_ng_output)
    c.save()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', required=True, help='Domain to scan')
    args = parser.parse_args()

    main(args.url)
