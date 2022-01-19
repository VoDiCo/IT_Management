import React, { Component } from "react";
import {DataGrid} from "@mui/x-data-grid";


const columns = [
    {field: 'device_id', headerName: 'ID'},
    {field: 'barcode', headerName: 'Barcode', maxWidth: 150, renderCell: (params)=><a href={params.value}><img src={params.value} width={100}/></a>},
    {field: 'device_type_name', headerName: 'Gerätetyp'},
    {field: 'manufacturer', headerName: 'Hersteller'}
]

export default class HomePage extends Component {
  constructor(props) {
    super(props);
    }

    state = {
        data: [],
        isLoaded: false
    };


async componentDidMount() {
    try{
        const response =await fetch('http://127.0.0.1:8000/api/device/');
        const data = await response.json();
        console.log(data, 'also')
        this.setState({data : data, isLoaded : true});
    }catch (err){
        console.log(err)
    }
}


  render() {
      const {data, isLoaded} = this.state;
      console.log(data, 'here we go')
      return (
          <div style={{height: 400, width: '100%'}}>
              {!isLoaded ? <div>Loading . . .</div> :
                  <DataGrid
                      getRowId={data => data.device_id}
                      rows={data}
                      columns={columns}
                      pageSize={5}
                      rowsPerPageOptions={[5]}
                      checkboxSelection
                  />
              }
          </div>
      );

  }
}
