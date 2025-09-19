import { Link } from "react-router-dom";
import { HiOutlineViewGrid, HiOutlineCube, HiOutlineCreditCard, HiX } from "react-icons/hi";

export default function Sidebar({ isOpen, toggleSidebar }) {
  return (
    <aside
      className={`fixed top-0 left-0 h-screen w-64 bg-white shadow-lg p-4 z-50 transform transition-transform duration-300 ease-in-out
      ${isOpen ? 'translate-x-0' : '-translate-x-full'}
      md:hidden`}
    >
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-2xl font-bold text-orange-500">Menu</h2>
        <button onClick={toggleSidebar} className="text-gray-600 hover:text-orange-500">
          <HiX size={24} />
        </button>
      </div>
      <ul className="space-y-2">
        <li>
          <Link
            to="/"
            onClick={toggleSidebar}
            className="flex items-center space-x-3 px-3 py-2 rounded-md text-gray-700 hover:bg-orange-100 hover:text-orange-600"
          >
            <HiOutlineViewGrid size={20} />
            <span>Dashboard</span>
          </Link>
        </li>
        <li>
          <Link
            to="/products"
            onClick={toggleSidebar}
            className="flex items-center space-x-3 px-3 py-2 rounded-md text-gray-700 hover:bg-orange-100 hover:text-orange-600"
          >
            <HiOutlineCube size={20} />
            <span>Products</span>
          </Link>
        </li>
        <li>
          <Link
            to="/transactions"
            onClick={toggleSidebar}
            className="flex items-center space-x-3 px-3 py-2 rounded-md text-gray-700 hover:bg-orange-100 hover:text-orange-600"
          >
            <HiOutlineCreditCard size={20} />
            <span>Transactions</span>
          </Link>
        </li>
      </ul>
    </aside>
  );
}