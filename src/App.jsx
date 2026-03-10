import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import axios from 'axios'

function App() {
  const [value, setValue] = useState(0)
  const [data, setData] = useState(null)
  const [isFetched, setIsFetched] = useState(false)

  useEffect(() => {
    setIsFetched(false)
    axios.get("https://api.restful-api.dev/objects").then(res => {
      setData(res?.data)
      setIsFetched(true)
    })
  }, [])

  return (
    <>
      <div className>
        {/* <Card data = {data?.[Math.floor(Math.random() * data?.length)]} isFetched={isFetched}/> */}
          {data?.map((item) => (
              <div className='pam'>
                <Card key={item.id} data={item} isFetched={isFetched} />
              </div>
          ))}
      </div>
    </>
  )
}
  const Card = ({data,isFetched}) => {
  const [options, setOptions] = useState([])

  useEffect(() =>{
    if(data){
      const res = getOptions(data?.data)
      setOptions(res)
    }
  }, [data])

  const getOptions = (options) =>{
    if(!options) return []

    let resArr = []
    let keys = Object.keys(options)

    return keys.map(key => ({label: key, value: options[key]}))
  }
  if(!isFetched) return 'Loading...'
  return (
    <div>
      <div className = "t">
       {data?.name}
      </div>
      {options?.map((el,zn) => (
        <div key = {zn}>
          <strong>{el?.label}</strong>
          <span>{el?.value}</span>
        </div>
      ))}
    </div>
  )
}
export default App
