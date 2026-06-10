import { useState } from "react";
import { generateAutomation } from "../api/workflowApi";
import CodeBox from "./CodeBox";
import Loader from "./Loader";
import "./AutomationGenerator.css";

export default function AutomationGenerator({
  repoContext,
  testCases,
  onGenerationComplete,
  onLoading,
}) {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [automationCode, setAutomationCode] = useState(null);
  const [activeTab, setActiveTab] = useState("preview");

  const handleGenerate = async () => {
    if (!testCases || testCases.length === 0) {
      setError("Please generate test cases first");
      return;
    }

    if (!repoContext) {
      setError("Repository context is missing");
      return;
    }

    setLoading(true);
    setError("");
    onLoading?.(true);

    try {
      const result = await generateAutomation(
        repoContext,
        testCases,
        repoContext.project_name || "TestProject"
      );

      if (result.status === "error") {
        setError(result.error || "Failed to generate automation code");
        return;
      }

      setAutomationCode(result);
      onGenerationComplete?.(result);
    } catch (err) {
      setError(
        err.error || err.message || "Failed to generate automation code"
      );
    } finally {
      setLoading(false);
      onLoading?.(false);
    }
  };

  return (
    <div className="automation-generator">
      <div className="generator-card">
        <h2>Automation Code Generator</h2>
        <p className="subtitle">Convert manual test cases into executable automation code</p>

        {!testCases || testCases.length === 0 && (
          <div className="warning-message">
            ⚠️ Please generate test cases first to proceed
          </div>
        )}

        <div className="info-box">
          <span className="info-label">Framework:</span>
          <span className="info-value">
            {repoContext?.framework || "Auto-detect"}
          </span>
          <span className="info-label">Language:</span>
          <span className="info-value">
            {repoContext?.language || "Auto-detect"}
          </span>
          {testCases && (
            <>
              <span className="info-label">Test Cases:</span>
              <span className="info-value">{testCases.length}</span>
            </>
          )}
        </div>

        {error && <span className="error-message">{error}</span>}

        <button
          onClick={handleGenerate}
          disabled={loading || !testCases || testCases.length === 0}
          className="generate-btn"
        >
          {loading ? (
            <>
              <Loader size={16} style={{ marginRight: "8px" }} />
              Generating...
            </>
          ) : (
            "Generate Automation Code"
          )}
        </button>

        {automationCode && (
          <div className="automation-results">
            <div className="results-header">
              <h3>Generated Code</h3>
              <div className="result-stats">
                <div className="stat">
                  <span className="label">Framework:</span>
                  <span className="value">{automationCode.framework}</span>
                </div>
                <div className="stat">
                  <span className="label">Language:</span>
                  <span className="value">{automationCode.language}</span>
                </div>
                <div className="stat">
                  <span className="label">Lines:</span>
                  <span className="value">{automationCode.total_lines || 0}</span>
                </div>
                <div className="stat">
                  <span className="label">Tests:</span>
                  <span className="value">
                    {automationCode.generated_files?.[0]?.test_count || 0}
                  </span>
                </div>
              </div>
            </div>

            <div className="tabs">
              <button
                className={`tab-btn ${activeTab === "preview" ? "active" : ""}`}
                onClick={() => setActiveTab("preview")}
              >
                Code Preview
              </button>
              <button
                className={`tab-btn ${activeTab === "files" ? "active" : ""}`}
                onClick={() => setActiveTab("files")}
              >
                Generated Files
              </button>
            </div>

            {activeTab === "preview" && automationCode.code && (
              <div className="code-preview">
                <CodeBox code={automationCode.code} language="python" />
              </div>
            )}

            {activeTab === "files" && automationCode.generated_files && (
              <div className="files-list">
                {automationCode.generated_files.map((file, idx) => (
                  <div key={idx} className="file-item">
                    <div className="file-header">
                      <span className="file-name">📄 {file.filename}</span>
                      <span className="file-meta">
                        {file.language} • {file.framework}
                      </span>
                    </div>
                    <div className="file-info">
                      <span>
                        <strong>Path:</strong> {file.file_path}
                      </span>
                      <span>
                        <strong>Tests:</strong> {file.test_count}
                      </span>
                      <span>
                        <strong>Size:</strong> {(file.content_length / 1024).toFixed(2)} KB
                      </span>
                    </div>
                  </div>
                ))}
              </div>
            )}

            <div className="next-step">
              <p>✅ Automation code ready! Ready to execute the tests?</p>
              <p className="hint">Proceed to the next step to run the tests.</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
