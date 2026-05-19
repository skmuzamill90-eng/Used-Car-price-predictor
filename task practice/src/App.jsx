export default function App() {
  return (
    <div className="min-h-screen bg-gray-200 flex justify-center items-center">

      <div className="bg-white p-8 rounded-2xl shadow-xl w-96">

        <h1 className="text-3xl font-bold text-center mb-6">
          Profile Page
        </h1>

        <div className="space-y-4">

          <div className="flex justify-between">
            <span className="font-semibold">Name:</span>
            <span>Muzamill</span>
          </div>

          <div className="flex justify-between">
            <span className="font-semibold">Age:</span>
            <span>20</span>
          </div>

          <div className="flex justify-between">
            <span className="font-semibold">Salary:</span>
            <span>₹50,000</span>
          </div>

          <div className="flex justify-between">
            <span className="font-semibold">Role:</span>
            <span>Frontend Developer</span>
          </div>

          <div className="flex justify-between">
            <span className="font-semibold">Location:</span>
            <span>India</span>
          </div>

        </div>

        <button className="w-full mt-6 bg-blue-600 text-white py-2 rounded-xl hover:bg-blue-700">
          Contact
        </button>

      </div>

    </div>
  )
}