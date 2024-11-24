import { CalendarIcon } from "lucide-react"
import { Badge } from "@/components/ui/badge"

interface Todo {
  id: number
  name: string
  description: string
  dueDate: string
  priority: string
}

interface TodoItemProps {
  todo: Todo
}

export function TodoItem({ todo }: TodoItemProps) {
  const priorityColor = {
    High: "bg-red-100 text-red-800",
    Medium: "bg-yellow-100 text-yellow-800",
    Low: "bg-green-100 text-green-800",
  }[todo.priority]

  return (
    <div className="mb-4 p-4 border rounded-lg hover:shadow-md transition-shadow">
      <h3 className="text-lg font-semibold mb-2">{todo.name}</h3>
      <p className="text-gray-600 mb-2">{todo.description}</p>
      <div className="flex items-center justify-between">
        <div className="flex items-center space-x-2">
          <CalendarIcon className="h-4 w-4 text-gray-400" />
          <span className="text-sm text-gray-500">{todo.dueDate}</span>
        </div>
        <Badge className={`${priorityColor}`}>{todo.priority}</Badge>
      </div>
    </div>
  )
}

