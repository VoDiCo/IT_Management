import React, { Component } from "react";
import {DataGrid, GridToolbar} from "@mui/x-data-grid";


const urls = 'http://127.0.0.1:8000/api/device/'

const columns = [
    {field: 'device_id', headerName: 'ID', hide: true},
    {field: 'barcode', headerName: 'Barcode', maxWidth: 150, renderCell: (params)=><a href={params.value}><img src={params.value} width={100}/></a>},
    {field: 'device_type_name', headerName: 'Gerätetyp'},
    {field: 'manufacturer', headerName: 'Hersteller'}
]

export default class Devices extends Component {
  constructor(props) {
    super(props);
    }

    state = {
        data: [],
        isLoaded: false
    };


async componentDidMount() {
    try{
        const response =await fetch(urls);
        const data = await response.json();
        this.setState({data : data, isLoaded : true});
    }catch (err){
        console.log(err)
    }
}


  render() {
      const {data, isLoaded} = this.state;
      return (
          <div style={{height: 400, width: '100%'}}>
              {!isLoaded ? <div>Loading . . .</div> :
                  <DataGrid
                      getRowId={data => data.device_id}
                      rows={data}
                      columns={columns}
                      pageSize={10}
                      rowsPerPageOptions={[10]}
                      checkboxSelection
                      components={
                          {Toolbar: GridToolbar}
                      }
                      disableColumnMenu
                      localeText={
                        {
                          toolbarDensity: 'Größe',
                          toolbarDensityLabel: 'Größe',
                          toolbarDensityCompact: 'Kompakt',
                          toolbarDensityStandard: 'Standard',
                          toolbarDensityComfortable: 'Komfortabel',
                        }
                      }
                  />
              }
          </div>
      );

  }
}
