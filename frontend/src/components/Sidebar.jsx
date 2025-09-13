import { Link } from "react-router-dom";

export default function Sidebar() {
  return (
    <aside className="w-64 bg-gray-100 h-screen shadow-md p-4">
      <ul className="space-y-2">
        <li>
          <Link to="/" className="block px-3 py-2 rounded hover:bg-gray-200">
            Dashboard
          </Link>
        </li>
        <li>
          <Link to="/products" className="block px-3 py-2 rounded hover:bg-gray-200">
            Products
          </Link>
        </li>
        <li>
          <Link to="/transactions" className="block px-3 py-2 rounded hover:bg-gray-200">
            Transactions
          </Link>
        </li>
      </ul>
    </aside>
  );
}
