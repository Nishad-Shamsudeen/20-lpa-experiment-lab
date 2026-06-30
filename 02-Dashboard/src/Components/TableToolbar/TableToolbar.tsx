import React from 'react'
import './TableToolbar.css'
function TableToolbar() {
  return (
    <div className=' flex h-12 justify-between bg-rose-200'>
        <div>
            <h3>Attonation Workflows</h3>
        </div>
        <div>
            <input type="text" placeholder="Search.." className='search'/>
        </div>
        </div>
  )
}

export default TableToolbar