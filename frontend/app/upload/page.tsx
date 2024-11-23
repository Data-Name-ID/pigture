'use client'

import { useState } from 'react'
import FileUploadProgress from '@/components/file-upload-progress'
import { Button } from "@/components/ui/button"

export default function UploadPage() {
  const [isUploading, setIsUploading] = useState(false)

  const simulateFileUpload = (onProgress: (progress: number) => void) => {
    let progress = 0
    const interval = setInterval(() => {
      progress += Math.random() * 10
      if (progress > 100) progress = 100
      onProgress(progress)
      if (progress === 100) {
        clearInterval(interval)
        setIsUploading(false)
      }
    }, 500)
  }

  const handleUpload = () => {
    setIsUploading(true)
    // Simulate a file upload of 100MB
    simulateFileUpload((progress) => {
      // This function will be called by the FileUploadProgress component
      // to update the progress
    })
  }

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center p-4">
      <h1 className="text-2xl font-bold mb-4">File Upload Demo</h1>
      <Button onClick={handleUpload} disabled={isUploading} className="mb-4">
        {isUploading ? 'Uploading...' : 'Start Upload'}
      </Button>
      {isUploading && (
        <FileUploadProgress
          fileName="large-file.zip"
          fileSize={100 * 1024 * 1024} // 100MB
          onProgress={(callback) => simulateFileUpload(callback)}
          onComplete={() => console.log('Upload completed')}
          onError={() => console.error('Upload failed')}
        />
      )}
    </div>
  )
}

