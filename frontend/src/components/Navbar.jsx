import { useState } from "react";
import { Link, useLocation } from "react-router-dom";
import { HiMenuAlt2, HiOutlineUserCircle } from "react-icons/hi";

export default function Navbar({ toggleSidebar }) {
  const [dropdownOpen, setDropdownOpen] = useState(false);
  const location = useLocation();

  const getLinkClass = (path) => {
    return `px-4 py-2 rounded-md transition-colors ${
      location.pathname === path
        ? "bg-orange-500 text-white font-semibold"
        : "text-gray-700 hover:bg-orange-100 hover:text-orange-600"
    }`;
  };

  return (
    <nav className="bg-white shadow-md px-4 py-3 flex justify-between items-center">
      <div className="flex items-center space-x-4">
        {/* Tombol ini hanya muncul di layar mobile */}
        <button
          onClick={toggleSidebar}
          className="text-gray-600 md:hidden p-2 rounded-full hover:bg-gray-100"
        >
          <HiMenuAlt2 size={24} />
        </button>
        <h1 className="text-xl font-bold text-orange-500">Toko Rabay Orange</h1>
      </div>

      {/* Navigasi Desktop - hanya muncul di desktop */}
      <div className="hidden md:flex items-center space-x-2">
        <Link to="/" className={getLinkClass("/")}>
          Dashboard
        </Link>
        <Link to="/products" className={getLinkClass("/products")}>
          Products
        </Link>
        <Link to="/transactions" className={getLinkClass("/transactions")}>
          Transactions
        </Link>
      </div>

      <div className="relative">
        <button
          onClick={() => setDropdownOpen(!dropdownOpen)}
          className="flex items-center space-x-2 text-gray-600 hover:text-orange-500"
        >
          <span className="hidden md:block">Halo, Admin!</span>
          <HiOutlineUserCircle size={24} />
        </button>
        {dropdownOpen && (
          <div className="absolute right-0 mt-2 w-48 bg-white rounded-md shadow-lg py-1 z-10">
            <Link
              to="/profile"
              className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
            >
              Profil
            </Link>
            <button className="block w-full text-left px-4 py-2 text-sm text-red-500 hover:bg-gray-100">
              Logout
            </button>
          </div>
        )}
      </div>
    </nav>
  );
}