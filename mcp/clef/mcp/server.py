"""MCP server: tool `clef_decide` gọi cổng Clef. Chạy: python mcp/clef/mcp/server.py (stdio).

Biến môi trường (chỉ tên): CLEF_GATE_URL, CLEF_CALLER (một tên trong ALLOWED_CALLERS), CLEF_CALLER_SECRET, CLEF_TIMEOUT_S.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "batch"))
import clef_batch  # noqa: E402

_CACHE = {}


def clef_decide(questions: dict, state: dict | None = None, model: str = "clef",
                context_version: str = "0", qset_version: str = "0", send=None) -> dict:
    """Hỏi Clef các câu noul/choice/score. Lỗi bất kỳ -> fallback=true, bên gọi tự quyết theo luật cũ."""
    if send is None:
        send = clef_batch.gui_http(os.environ.get("CLEF_GATE_URL", "https://clef.example.com"),
                                   os.environ.get("CLEF_CALLER", ""), os.environ.get("CLEF_CALLER_SECRET", ""),
                                   float(os.environ.get("CLEF_TIMEOUT_S", "10")))
    return clef_batch.quyet_dinh(questions, send, state=state, model=model, context_version=context_version,
                                 qset_version=qset_version, cache=_CACHE, max_calls=4)


def main():
    try:  # mcp 2.x
        from mcp.server.mcpserver import MCPServer as Server
    except ImportError:  # mcp 1.x
        from mcp.server.fastmcp import FastMCP as Server
    app = Server("clef")

    @app.tool(name="clef_decide")
    def _tool(questions: dict, state: dict | None = None, model: str = "clef",
              context_version: str = "0", qset_version: str = "0") -> dict:
        """Hỏi Clef (noul/choice/score, tự chia lô <=64). Trả answers + fallback."""
        return clef_decide(questions, state, model, context_version, qset_version)

    app.run()


if __name__ == "__main__":
    main()
