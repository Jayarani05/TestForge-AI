import { useState } from "react";
import { generateTestCases } from "../api/workflowApi";
import Loader from "./Loader";
import "./TestCaseGenerator.css";

export default function TestCaseGenerator({
  repoContext,
  onGenerationComplete,
  onLoading,
}) {
  const [userStory, setUserStory] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [testCases, setTestCases] = useState(null);

  const handleGenerate = async () => {
    if (!userStory.trim()) {
      setError("Please enter a user story");
      return;
    }

    if (!repoContext) {
      setError("Please analyze a repository first");
      return;
    }

    setLoading(true);
    setError("");
    onLoading?.(true);

    try {
      const result = await generateTestCases(repoContext, userStory.trim());

      if (result.status === "error") {
        setError(result.error || "Failed to generate test cases");
        return;
      }

      setTestCases(result);
      onGenerationComplete?.(result);
    } catch (err) {
      setError(err.error || err.message || "Failed to generate test cases");
    } finally {
      setLoading(false);
      onLoading?.(false);
    }
  };

  return (
    <div className="test-case-generator">
      <div className="generator-card">
        <h2>Test Case Generator</h2>
        <p className="subtitle">Generate QA test cases from your user story</p>

        {!repoContext && (
          <div className="warning-message">
            ⚠️ Please analyze a repository first to get started
          </div>
        )}

        <div className="input-group">
          <label>User Story</label>
          <textarea
            placeholder="Example: As a user, I want to login with my email and password so that I can access the dashboard..."
            value={userStory}
            onChange={(e) => {
              setUserStory(e.target.value);
              setError("");
            }}
            disabled={loading || !repoContext}
            className={error ? "textarea-error" : ""}
            rows={6}
          />
          {error && <span className="error-message">{error}</span>}
        </div>

        <button
          onClick={handleGenerate}
          disabled={loading || !userStory.trim() || !repoContext}
          className="generate-btn"
        >
          {loading ? (
            <>
              <Loader size={16} style={{ marginRight: "8px" }} />
              Generating...
            </>
          ) : (
            "Generate Test Cases"
          )}
        </button>

        {testCases && testCases.test_cases && (
          <div className="test-cases-results">
            <div className="results-header">
              <h3>Generated Test Cases</h3>
              <div className="summary-stats">
                <div className="stat">
                  <span className="stat-label">Total</span>
                  <span className="stat-value">{testCases.summary?.total || 0}</span>
                </div>
                <div className="stat positive">
                  <span className="stat-label">Positive</span>
                  <span className="stat-value">{testCases.summary?.positive || 0}</span>
                </div>
                <div className="stat negative">
                  <span className="stat-label">Negative</span>
                  <span className="stat-value">{testCases.summary?.negative || 0}</span>
                </div>
                <div className="stat edge">
                  <span className="stat-label">Edge Cases</span>
                  <span className="stat-value">{testCases.summary?.edge_cases || 0}</span>
                </div>
              </div>
            </div>

            <div className="test-cases-grid">
              {testCases.test_cases.map((testCase, idx) => (
                <div
                  key={idx}
                  className={`test-case-card category-${testCase.category}`}
                >
                  <div className="card-header">
                    <span className="test-id">{testCase.id}</span>
                    <span className={`priority priority-${testCase.priority.toLowerCase()}`}>
                      {testCase.priority}
                    </span>
                    <span className="category-badge">{testCase.category}</span>
                  </div>

                  <h4>{testCase.title}</h4>
                  <p className="description">{testCase.description}</p>

                  <div className="steps">
                    <span className="steps-label">Steps:</span>
                    <ol>
                      {testCase.steps.map((step, stepIdx) => (
                        <li key={stepIdx}>{step}</li>
                      ))}
                    </ol>
                  </div>

                  <div className="expected-result">
                    <span className="label">Expected Result:</span>
                    <p>{testCase.expected_result}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
