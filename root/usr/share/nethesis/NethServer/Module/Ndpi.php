<?php

namespace NethServer\Module;

/*
 * Copyright (C) 2016 Nethesis S.r.l.
 * 
 * This script is part of NethServer.
 * 
 * NethServer is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * NethServer is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with NethServer.  If not, see <http://www.gnu.org/licenses/>.
 */

use Nethgui\System\PlatformInterface as Validate;

/**
 * Display nDPI protocols
 *
 * @author Giacomo Sanchietti
 *
 */
class Ndpi extends \Nethgui\Controller\TableController
{

    protected function initializeAttributes(\Nethgui\Module\ModuleAttributesInterface $base)
    {
        return \Nethgui\Module\SimpleModuleAttributesProvider::extendModuleAttributes($base, 'Status');
    }


    public function initialize()
    {
        $columns = array(
            'Key',
            'count',
        );

        $this
            ->setTableAdapter($this->getPlatform()->getTableAdapter('NethServer::Database::Ndpi', 'ndpi'))
            ->setColumns($columns)
        ;

        parent::initialize();
    }


    public function prepareViewForColumnKey(\Nethgui\Controller\Table\Read $action, \Nethgui\View\ViewInterface $view, $key, $values, &$rowMetadata)
    {
        $name = \NethServer\Module\FirewallRules\Index::resolveNdpiName($key);
        return ' <i class="fa fa-lg '.\NethServer\Module\FirewallRules\Index::getNdpiIconName($name).'" aria-hidden="true" style="margin: 5px"></i>' . "$name ($key)" ;
    }

}
