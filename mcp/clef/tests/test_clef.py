"""Test offline cho batch + MCP tool. Chạy: python3 -m unittest discover -s mcp/clef/tests"""
import os
import socket
import sys
import unittest

GOC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path[:0] = [os.path.join(GOC, "batch"), os.path.join(GOC, "mcp")]
import clef_batch  # noqa: E402
import server  # noqa: E402


class GiaClef:
    """Cổng giả: đếm lần gọi, trả lời theo loại câu."""
    def __init__(self):
        self.lo = []

    def __call__(self, payload):
        self.lo.append(len(payload["questions"]))
        tra = {"noul": {"type": "noul", "noul": 0.9},
               "score": {"type": "score", "score": 1.0, "confidence": 0.8, "probabilities": {}},
               "choice": {"type": "choice", "choice": "sale", "confidence": 0.7, "probabilities": {}}}
        return {"answers": {k: tra[q["type"]] for k, q in payload["questions"].items()}, "fallback": False}


def cau(n, loai="noul"):
    return {f"q{i}": {"type": loai, "instructions": f"Câu {i}?"} for i in range(n)}


class TestBatch(unittest.TestCase):
    def test_chia_lo_64(self):
        g = GiaClef()
        r = clef_batch.quyet_dinh(cau(130), g)
        self.assertEqual(g.lo, [64, 64, 2])
        self.assertFalse(r["fallback"])
        self.assertEqual(len(r["answers"]), 130)

    def test_lo_65_bi_tu_choi_truoc_khi_gui(self):
        g = GiaClef()
        with self.assertRaises(clef_batch.LoQuaLon):
            clef_batch.goi_mot_lo(g, cau(65), {}, "clef", "c", "q")
        self.assertEqual(g.lo, [])

    def test_ba_loai_cau(self):
        qs = {"a": {"type": "noul", "instructions": "?"}, "b": {"type": "score", "instructions": "?"},
              "c": {"type": "choice", "instructions": "?", "criteria": {"sale": "x", "bo_qua": "y"}}}
        r = clef_batch.quyet_dinh(qs, GiaClef())
        self.assertEqual([r["answers"][k]["type"] for k in "abc"], ["noul", "score", "choice"])

    def test_cache_theo_text_ctx_qset_model(self):
        g, cache = GiaClef(), {}
        clef_batch.quyet_dinh(cau(3), g, cache=cache)
        clef_batch.quyet_dinh(cau(3), g, cache=cache)
        self.assertEqual(g.lo, [3])
        clef_batch.quyet_dinh(cau(3), g, cache=cache, qset_version="q-2")
        clef_batch.quyet_dinh(cau(3), g, cache=cache, model="clef-flash")
        self.assertEqual(g.lo, [3, 3, 3])

    def test_tran_so_lan_goi(self):
        g = GiaClef()
        r = clef_batch.quyet_dinh(cau(200), g, max_calls=2)
        self.assertEqual(g.lo, [64, 64])
        self.assertTrue(r["fallback"])
        self.assertIn("het-luot-goi", r["reasons"])
        self.assertIsNone(r["answers"]["q199"])

    def test_mat_mang_fallback(self):
        def dut(_):
            raise ConnectionError("network down")
        r = clef_batch.quyet_dinh(cau(2), dut)
        self.assertTrue(r["fallback"])
        self.assertEqual(r["answers"], {"q0": None, "q1": None})


class TestMcp(unittest.TestCase):
    def test_tool_mat_mang_that_fallback(self):
        s = socket.socket()
        s.bind(("127.0.0.1", 0))
        cong = s.getsockname()[1]
        s.close()  # cổng đóng -> ConnectionRefused, không ra mạng ngoài
        os.environ.update(CLEF_GATE_URL=f"http://127.0.0.1:{cong}", CLEF_CALLER="caller-a",
                          CLEF_CALLER_SECRET="test-secret-a", CLEF_TIMEOUT_S="1")
        r = server.clef_decide(cau(1, "choice"), qset_version="mcp-1")
        self.assertTrue(r["fallback"])

    def test_tool_tra_loi(self):
        r = server.clef_decide(cau(2, "score"), send=GiaClef(), qset_version="mcp-2")
        self.assertEqual(r["answers"]["q1"]["type"], "score")


if __name__ == "__main__":
    unittest.main()
