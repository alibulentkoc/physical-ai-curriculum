"""Emit Module 9 quizzes in the repo's standard self-contained format."""
import json, os

HEAD = ('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        '<title>Knowledge Check \u2014 Lesson @@LESSON@@</title>\n'
        '<script>window.MathJax={tex:{inlineMath:[["$","$"],["\\\\(","\\\\)"]],'
        'displayMath:[["$$","$$"],["\\\\[","\\\\]"]]}};</script>\n'
        '<script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>\n'
        '<style>\n'
        ':root{--ink:#0f172a;--muted:#64748b;--line:#e2e8f0;--soft:#f8fafc;--green:#15803d;'
        '--greenbg:#dcfce7;--red:#b91c1c;--redbg:#fee2e2;--accent:#0d9488;}\n'
        '*{box-sizing:border-box}body{margin:0;font-family:Segoe UI,Helvetica,Arial,sans-serif;'
        'color:var(--ink);background:transparent}\n'
        '.wrap{max-width:760px;margin:0 auto;padding:6px}\n'
        '.note{font-size:13px;color:var(--muted);background:var(--soft);border:1px solid var(--line);'
        'border-radius:10px;padding:10px 12px;margin-bottom:14px}\n'
        '.q{border:1px solid var(--line);border-radius:12px;padding:14px 16px;margin:12px 0;background:#fff}\n'
        '.qhead{font-weight:600;font-size:14.5px;margin-bottom:10px}.qnum{display:inline-block;'
        'min-width:22px;color:var(--accent);font-weight:700}\n'
        '.opt{display:block;width:100%;text-align:left;border:1px solid var(--line);background:#fff;'
        'border-radius:9px;padding:9px 12px;margin:6px 0;font-size:14px;cursor:pointer}\n'
        '.opt:hover{background:var(--soft)}.opt.correct{background:var(--greenbg);border-color:#86efac;'
        'color:var(--green);font-weight:600}.opt.wrong{background:var(--redbg);border-color:#fecaca;color:var(--red)}\n'
        '.fb{font-size:13px;margin-top:8px;padding:8px 10px;border-radius:8px;display:none}.fb.show{display:block}'
        '.fb.ok{background:var(--greenbg);color:var(--green)}.fb.no{background:var(--redbg);color:var(--red)}'
        '.fb.info{background:#eff6ff;color:#1d4ed8}\n'
        'textarea{width:100%;min-height:60px;border:1px solid var(--line);border-radius:9px;padding:8px;'
        'font-family:inherit;font-size:14px;resize:vertical}\n'
        '.btn{appearance:none;border:1px solid var(--line);background:#fff;border-radius:9px;padding:7px 13px;'
        'font-size:13.5px;font-weight:600;cursor:pointer;margin-top:8px}.btn:hover{background:var(--soft)}\n'
        '.model{display:none;font-size:13px;margin-top:8px;padding:8px 10px;border-radius:8px;'
        'background:#eff6ff;color:#1d4ed8}.model.show{display:block}\n'
        '</style></head><body><div class="wrap">\n'
        '<div class="note">Formative \u2014 unlimited attempts, immediate feedback. This does <b>not</b> affect your grade.</div>\n'
        '<div id="quiz"></div></div>\n'
        '<script>var questions=')

TAIL = (';\n'
        'var root=document.getElementById("quiz");\n'
        'questions.forEach(function(q,i){var card=document.createElement("div");card.className="q";\n'
        'var head=document.createElement("div");head.className="qhead";head.innerHTML=\'<span class="qnum">\'+(i+1)+\'.</span> \'+q.prompt;card.appendChild(head);\n'
        'var fb=document.createElement("div");fb.className="fb";\n'
        'if(q.type==="mc"||q.type==="tf"){var opts=q.type==="tf"?[{t:"True",ok:q.answer===true},{t:"False",ok:q.answer===false}]:q.options;\n'
        'opts.forEach(function(o){var b=document.createElement("button");b.className="opt";b.type="button";b.innerHTML=o.t;\n'
        'b.addEventListener("click",function(){Array.prototype.forEach.call(card.querySelectorAll(".opt"),function(el){el.classList.remove("correct","wrong");});\n'
        'if(o.ok){b.classList.add("correct");fb.className="fb show ok";fb.innerHTML=q.ok;}else{b.classList.add("wrong");fb.className="fb show no";fb.innerHTML=q.no;}});card.appendChild(b);});card.appendChild(fb);}\n'
        'else if(q.type==="short"){var ta=document.createElement("textarea");ta.placeholder="Type your answer, then reveal the model answer to self-check\u2026";card.appendChild(ta);\n'
        'var sh=document.createElement("button");sh.className="btn";sh.type="button";sh.textContent="Show model answer";var md=document.createElement("div");md.className="model";md.innerHTML=q.model;\n'
        'sh.addEventListener("click",function(){md.classList.toggle("show");sh.textContent=md.classList.contains("show")?"Hide model answer":"Show model answer";});card.appendChild(sh);card.appendChild(md);}\n'
        'root.appendChild(card);});\n'
        'if(window.MathJax&&MathJax.typesetPromise){MathJax.typesetPromise();}\n'
        '</script></body></html>\n')


def write_quiz(path, lesson_no, questions):
    html = HEAD.replace("@@LESSON@@", str(lesson_no)) + json.dumps(questions, ensure_ascii=False) + TAIL
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(html)
