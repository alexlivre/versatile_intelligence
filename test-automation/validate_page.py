import re, json
from html.parser import HTMLParser

class HTMLValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.errors = []
        self.tag_stack = []
        self.void_elements = {
            'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input',
            'link', 'meta', 'param', 'source', 'track', 'wbr'
        }

    def handle_starttag(self, tag, attrs):
        if tag.lower() not in self.void_elements:
            self.tag_stack.append((tag.lower(), self.getpos()))

    def handle_endtag(self, tag):
        tag_lower = tag.lower()
        if tag_lower in self.void_elements:
            return
        if not self.tag_stack:
            self.errors.append(f"Unexpected closing tag </{tag}> at line {self.getpos()[0]}")
            return
        last_tag, pos = self.tag_stack.pop()
        if last_tag != tag_lower:
            self.errors.append(f"Mismatched tag: expected </{last_tag}> (opened at line {pos[0]}), got </{tag}> at line {self.getpos()[0]}")

def run_tests():
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()

    # 1. HTML Syntax Validation
    validator = HTMLValidator()
    validator.feed(content)
    assert len(validator.errors) == 0, f"HTML errors: {validator.errors}"
    print("[PASS] HTML Syntax and Tag Structure")

    # 2. JSON-LD Validation
    matches = re.findall(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
    assert len(matches) > 0, "No JSON-LD found"
    for block in matches:
        data = json.loads(block)
        print(f"[PASS] JSON-LD block valid ({len(data)} items)")
        # Check member in Organization
        for item in data:
            if item.get("@type") == "Organization":
                members = item.get("member", [])
                assert any("Rafael Alves" in m.get("name", "") for m in members), "Member not found"
                print("[PASS] Organization member Rafael Alves confirmed in JSON-LD")

    # 3. Twitter Embed Validation
    assert '<blockquote class="twitter-tweet"' in content, "Twitter blockquote missing"
    assert "https://t.co/1OU4calJeU" in content, "t.co missing"
    assert "https://x.com/breno94es/status/2096680274637844547" in content, "x.com status missing"
    assert "platform.x.com/widgets.js" in content, "widgets.js missing"
    print("[PASS] Twitter / X Embed verified")

    # 4. Dossier Validation
    assert "Professor Rafael Alves da Silva" in content, "Name missing"
    assert "Escola SESI João Ubaldo Ribeiro" in content, "SESI school missing"
    assert "SESI Departamento Nacional" in content, "SESI DN missing"
    assert "Rede FIEB" in content, "FIEB missing"
    assert "Administrador" in content, "Admin status missing"
    assert "https://professorrafaelalves.com/" in content, "Professor website link missing"
    print("[PASS] Biography, credentials & official website link verified")

    # 5. FAQ 6 Validation
    assert "faq-answer-6" in content, "FAQ answer 6 missing"
    assert "Quem administra e modera a comunidade" in content, "FAQ 6 question missing"
    print("[PASS] FAQ item 6 verified")

    print("\n[SUCCESS] All verification tests passed (0 failures)!")

if __name__ == "__main__":
    run_tests()
