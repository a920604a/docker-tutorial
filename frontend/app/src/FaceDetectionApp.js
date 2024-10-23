import React, { useState } from 'react';

function FaceDetectionApp() {
    // 設定處理後的圖片和分析結果的狀態
    const [processedImage, setProcessedImage] = useState(null); // 存儲圖片的 Base64 字符串
    const [analysis, setAnalysis] = useState(null); // 存儲分析結果 (如人臉數量、座標等)

    const handleUpload = async (event) => {
        const file = event.target.files[0];
        const formData = new FormData();
        formData.append('file', file);

        // 發送圖片到後端進行處理

        const response = await fetch('http://localhost:8000/api/upload', {
            method: 'POST',
            body: formData,
        });

        const result = await response.json();
        console.log(result);

        // 更新處理後圖片和分析結果的狀態
        setProcessedImage(result.processedImage); // 假設是 Base64 格式的圖片數據
        setAnalysis(result.analysis); // 假設是 JSON 格式的分析數據
    };

    return (
        <div>
            <h1>人臉偵測系統</h1>
            <input type="file" onChange={handleUpload} />

            {/* 顯示上傳並處理後的圖片 */}
            {processedImage && (
                <div>
                    <h2>處理後的圖片：</h2>
                    <img src={`data:image/jpeg;base64,${processedImage}`} alt="Processed" />
                </div>
            )}

            {/* 顯示分析結果 */}
            {analysis && (
                <div>
                    <h2>偵測分析結果：</h2>
                    <pre>{JSON.stringify(analysis, null, 2)}</pre>
                </div>
            )}
        </div>
    );
}

export default FaceDetectionApp;
